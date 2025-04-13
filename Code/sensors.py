import time
import socket
from paho.mqtt import client as mqtt_client
import random
import logging
import json
import sys

import RPi.GPIO as GPIO # type: ignore
from datetime import datetime
from logic.sun_logic import get_location, get_sun_times
from logic.mqtt_client import connect_mqtt, on_disconnect
from logic.sensor_read import Sensor
from logic.emotion import Emotion

# Setup logging
logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger(__name__)
# initialize Sensors
my_sensors = Sensor()


# sensor script receives config via sys.argv
_LOGGER.info(f"arguments: {sys.argv}")
cfg={}
cfg = json.loads(sys.argv[1])
_LOGGER.info(f"config: {cfg}")

emotion_logic = Emotion(cfg)

# constants for mqtt
broker = cfg['MQTT Host']#'192.168.178.160'
port = int(cfg['MQTT Port'])#1883
topic = cfg['MQTT Topic']#"smart_pot/data"
emotion_topic = topic + "/emotion"
loc_topic = topic + "/location"
try:
    update_interval = int(cfg['MQTT Update Interval'])#360
except KeyError:
    _LOGGER.warning("No update interval configured. Using default (360s)")
    update_interval = 360
client_id = f'smart_pot-{random.randint(0, 1000)}'
username = cfg['MQTT Username']#'YOUR_USERNAME'
password = cfg['MQTT Password']#'YOUR_PASSWORD'
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


def mqtt_result_logging(topic, MQTT_MSG, status):
    if status == 0:
        _LOGGER.info(f"Send `{MQTT_MSG}` to topic `{topic}`")
    else:      
        _LOGGER.error(f"Failed to send message to topic {topic}")

try:
    #Setup Client for communication
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('0.0.0.0', int(cfg['Port'])))
    except Exception as e:
        _LOGGER.error(f"Could not connect to display socket: {e}")
        raise
    #Connect to MQTT
    mqtt_client = connect_mqtt(broker=broker, port=port, client_id=client_id, username=username, password=password)
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.loop_start()

    # location info
    city = get_location(cfg['Location'])#"Berlin"
    MQTT_MSG = json.dumps({"location": city.name})
    result = mqtt_client.publish(loc_topic, MQTT_MSG)
    status = result[0]
    mqtt_result_logging(loc_topic, MQTT_MSG, status)
    MQTT_MSG = ""
    last_execution_time = time.time()
    last_sun_calc_date = datetime.now().date()
    sunrise, sunset = get_sun_times(city=city)
    last_sent_state = None
    while True:
        now = datetime.now()
        # Check if the current date is different from the last calculated date
        if now.date() != last_sun_calc_date:
            sunrise, sunset = get_sun_times(city=city)
            last_sun_calc_date = now.date()
            _LOGGER.info(f"Recalculated sunrise/sunset for {last_sun_calc_date}")

        is_daytime = sunrise <= now.time() <= sunset

        if is_daytime:
            if last_sent_state == "black":
                Temperature, LDR_Percent, Moisture_Percent = my_sensors.read_sensor_data()
                emotion = emotion_logic.get_current_emotion(Temperature, LDR_Percent, Moisture_Percent)
                if emotion != last_sent_state:
                    client.send(bytes(f"{emotion}\n", 'utf-8'))
                    last_sent_state = emotion
                _LOGGER.info("Daylight resumed. Sending default emotion.")
        else:
            client.send(bytes('black\n', 'utf-8'))
            last_sent_state = "black"
            time.sleep(1)
            continue # Skip the rest of the loop if it's nighttime
        _LOGGER.info(f"Now: {now.time()}, Sunrise: {sunrise}, Sunset: {sunset}")
        # Read the specified ADC channels using the previously set gain value.
        Temperature, LDR_Percent, Moisture_Percent = my_sensors.read_sensor_data()
        emotion = emotion_logic.get_current_emotion(Temperature, LDR_Percent, Moisture_Percent) # get current emotion
        # Check if the emotion has changed
        if emotion != last_sent_state:
            _LOGGER.info(f"Sending {emotion}")
            client.send(bytes(f"{emotion}\n", 'utf-8'))
            last_sent_state = emotion
            MQTT_MSG=json.dumps({"emotion": emotion})
            result = mqtt_client.publish(emotion_topic, MQTT_MSG)
            status = result[0]
            mqtt_result_logging(topic, MQTT_MSG, status)
            MQTT_MSG = ""
        current_time = time.time()
        if current_time - last_execution_time >= update_interval:
            MQTT_MSG=json.dumps({"Temperature":Temperature,"Light Intensity":LDR_Percent,"Moisture %":Moisture_Percent})
            #send only every 360 seconds
            result = mqtt_client.publish(topic, MQTT_MSG)
            status = result[0]
            mqtt_result_logging(topic, MQTT_MSG, status)
            MQTT_MSG = ""
            last_execution_time = current_time
        time.sleep(1)
except KeyboardInterrupt:
    _LOGGER.info("Script interrupted by user (Ctrl+C). Cleaning up...")

except Exception as e:
    _LOGGER.exception(f"Unexpected error: {e}")
finally:
    try:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
    except Exception as e:
        _LOGGER.warning(f"MQTT cleanup failed: {e}")
    try:
        client.close()
    except Exception as e:
        _LOGGER.warning(f"Socket cleanup failed: {e}")
    try:
        GPIO.cleanup()
    except Exception as e:
        _LOGGER.warning(f"GPIO cleanup failed: {e}")
    _LOGGER.info("Cleanup done. Exiting.") 
