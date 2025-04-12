import time
import socket
import board
import busio
import adafruit_ads1x15.ads1115 as ADS # type: ignore
from adafruit_ads1x15.analog_in import AnalogIn # type: ignore
from w1thermsensor import W1ThermSensor # type: ignore

from paho.mqtt import client as mqtt_client
import random
import logging
import json
import sys

import RPi.GPIO as GPIO # type: ignore
from datetime import datetime
from sun_logic import get_location, get_sun_times
from mqtt_client import connect_mqtt, on_disconnect

# Setup logging
logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger(__name__)


# sensor script receives config via sys.argv
print(f"arguments: {sys.argv}")
_LOGGER.info(f"arguments: {sys.argv}")
cfg={}
cfg = json.loads(sys.argv[1])
print(f"config: {cfg}")
_LOGGER.info(f"config: {cfg}")
    

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
# Analog input channels may differ based on the connection
# use calibration.py to find the correct channel
Moisture_channel = AnalogIn(ads, ADS.P1)
LDR_channel = AnalogIn(ads, ADS.P2)
#LM35_channel = AnalogIn(ads, ADS.P3)
# Set up the backlight pin
BACKLIGHT_PIN = 18

# set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(BACKLIGHT_PIN, GPIO.OUT)

temp_sensor = W1ThermSensor()

ADC_16BIT_MAX = 65536
lm35_constant = 10.0/1000
ads_InputRange = 4.096 #For Gain = 1; Otherwise change accordingly
ads_bit_Voltage = (ads_InputRange * 2) / (ADC_16BIT_MAX - 1)

# min max values
LDR_Percent_min = int(cfg['Light Intensity min'])#20
LDR_Percent_max = int(cfg['Light Intensity max'])#20
Temperature_min = int(cfg['Temperature min'])#22
Temperature_max = int(cfg['Temperature max'])#30
Moisture_min = int(cfg['Moisture min'])#10
Moisture_max = int(cfg['Moisture max'])#90

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

def _map(x, in_min, in_max, out_min, out_max):
    """Map a value from one range to another."""
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def get_current_emotion(temperature, ldr_percent, moisture_percent):
    """Determine the current emotion based on temperature, light intensity, and moisture level."""
    # Priority-based emotion scoring system:
    #
    # | Emotion   | Meaning                    | Score |
    # |-----------|----------------------------|-------|
    # | freeze    | Critically cold            |   3   |
    # | hot       | Critically hot             |   3   |
    # | thirsty   | Low soil moisture          |   2   |
    # | hydrated    | Very moist soil            |   2   |
    # | sleepy    | Low light conditions       |   1   |
    # | happy     | Everything is fine         |   1   (default if no issues)
    #
    # Higher score = higher priority when multiple conditions match.
    # This ensures that more critical plant states are prioritized.
    scores = {
        "freeze": 0,
        "hot": 0,
        "thirsty": 0,
        "hydrated": 0,
        "sleepy": 0,
        "happy": 0,
    }
    # Check conditions and assign scores
    if temperature < Temperature_min:
        scores["freeze"] += 3
    elif temperature > Temperature_max:
        scores["hot"] += 3

    if moisture_percent < Moisture_min:
        scores["thirsty"] += 2
    elif moisture_percent > Moisture_max:
        scores["hydrated"] += 2

    if ldr_percent < LDR_Percent_min:
        scores["sleepy"] += 1

    if all(value == 0 for value in scores.values()):
        scores["happy"] = 1  # Standard

    # Determine the emotion with the highest score
    emotion = max(scores, key=scores.get)
    return emotion

def mqtt_result_logging(topic, MQTT_MSG, status):
    if status == 0:
        _LOGGER.info(f"Send `{MQTT_MSG}` to topic `{topic}`")
    else:      
        _LOGGER.error(f"Failed to send message to topic {topic}")

def read_sensor_data():
    ldr_val = LDR_channel.value
    ldr = _map(ldr_val, 22500, 50, 0, 100)
    moisture_val = Moisture_channel.value
    moisture = _map(moisture_val, 31000, 15500, 0, 100)
    temp = temp_sensor.get_temperature()
    return temp, ldr, moisture

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
                Temperature, LDR_Percent, Moisture_Percent = read_sensor_data()
                emotion = get_current_emotion(Temperature, LDR_Percent, Moisture_Percent)
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
        Temperature, LDR_Percent, Moisture_Percent = read_sensor_data()
        emotion = get_current_emotion(Temperature, LDR_Percent, Moisture_Percent) # get current emotion
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
        _LOGGER.debug(f"Temperature: {Temperature:.2f} °C")
        _LOGGER.debug(f"Light Intensity : {LDR_Percent} %")
        _LOGGER.debug(f"Moisture :{Moisture_Percent:.2f} %")
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
