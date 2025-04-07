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

#Initialising Variables
Moisture_Recent = 100
HighIn_DataSent = 0
LowIn_DataSent = 0
Thirsty_DataSent = 0
Savory_DataSent = 0
Happy_DataSent = 0
TemperatureDataSent = 0

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
cmd_topic = topic + "/cmd"
loc_topic = topic + "/location"
try:
    update_interval = int(cfg['MQTT Update Interval'])#360
except:
    update_interval = 360
client_id = f'smart_pot-{random.randint(0, 1000)}'
username = cfg['MQTT Username']#'YOUR_USERNAME'
password = cfg['MQTT Password']#'YOUR_PASSWORD'
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def backlight_on():
    """Switches the backlight ON"""
    GPIO.output(BACKLIGHT_PIN, GPIO.HIGH)
    _LOGGER.info("backlight ON")

def backlight_off():
    """Switches the backlight OFF"""
    GPIO.output(BACKLIGHT_PIN, GPIO.LOW)
    _LOGGER.info("backlight OFF")


# Map function
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
try:
    #Setup Client for communication
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', int(cfg['Port'])))

    #Connect to MQTT
    mqtt_client = connect_mqtt()
    mqtt_client.on_disconnect = on_disconnect
    mqtt_client.loop_start()

    # location info
    city = get_location(cfg['Location'])#"Berlin"
    MQTT_MSG = json.dumps({"location": city.name})
    result = mqtt_client.publish(loc_topic, MQTT_MSG)
    status = result[0]
    if status == 0:
        _LOGGER.info(f"Send `{MQTT_MSG}` to topic `{loc_topic}`")
    else:      
        _LOGGER.error(f"Failed to send message to topic {loc_topic}")

    MQTT_MSG = ""
    last_execution_time = time.time()
    last_sun_calc_date = datetime.now().date()
    sunrise, sunset = get_sun_times()
    while True:
        now = datetime.now()
        now = datetime.now()
        # Check if the current date is different from the last calculated date
        if now.date() != last_sun_calc_date:
            sunrise, sunset = get_sun_times()
            last_sun_calc_date = now.date()
            _LOGGER.info(f"Recalculated sunrise/sunset for {last_sun_calc_date}")

        is_daytime = sunrise <= now.time() <= sunset
        if is_daytime:
            backlight_on()
        else:
            backlight_off()
            client.send(bytes('black\n', 'utf-8'))  # oder 'blank\n', je nachdem wie du es im showimage/show behandelst
            continue # Skip the rest of the loop if it's nighttime
        # Read the specified ADC channels using the previously set gain value.
        LDR_Value = LDR_channel.value
        LDR_Percent = _map(LDR_Value, 22500, 50, 0, 100)
        Moisture_Value = Moisture_channel.value
        Moisture_Percent = _map(Moisture_Value, 31000, 15500, 0, 100)
        Temperature =  temp_sensor.get_temperature()
        _LOGGER.info(f"Temperature: {Temperature:.2f} °C")
        _LOGGER.info(f"Light Intensity : {LDR_Percent} %")
        _LOGGER.info(f"Moisture :{Moisture_Percent:.2f} %")
        current_time = time.time()
        if current_time - last_execution_time >= update_interval:
            MQTT_MSG=json.dumps({"Temperature":Temperature,"Light Intensity":LDR_Percent,"Moisture %":Moisture_Percent})
            #send only every 360 seconds
            result = mqtt_client.publish(topic, MQTT_MSG)
            status = result[0]
            if status == 0:
                _LOGGER.info(f"Send `{MQTT_MSG}` to topic `{topic}`")
            else:      
                _LOGGER.error(f"Failed to send message to topic {topic}")
            last_execution_time = current_time
        if (LDR_Percent < LDR_Percent_min):
            if(LowIn_DataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending sleepy")
                client.send(bytes('sleepy\n','utf-8'))
                #client.close()
                HighIn_DataSent = 0
                LowIn_DataSent = 1
        elif (LDR_Percent > LDR_Percent_min):
            if(HighIn_DataSent == 0):
                print("High Intensity")
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending happy")
                client.send(bytes('happy\n','utf-8'))
                #client.close()
                HighIn_DataSent = 1
                LowIn_DataSent = 0
            
        if (Moisture_Percent < Moisture_min):
            Moisture_Recent = Moisture_Percent
            if(Thirsty_DataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending thirsty")
                client.send(bytes('thirsty\n','utf-8'))
                #client.close()
                Thirsty_DataSent = 1
                Savory_DataSent = 0
                Happy_DataSent = 0
        elif (Moisture_Percent>Moisture_min and Moisture_Recent < Moisture_Percent and Moisture_Percent < Moisture_max):
            Moisture_Recent = Moisture_Percent
            if(Savory_DataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending savory")
                client.send(bytes('savory\n','utf-8'))
                #client.close()
                Savory_DataSent = 1
                Thirsty_DataSent = 0
                Happy_DataSent = 0
        elif (Moisture_Percent > Moisture_max):
            Moisture_Recent = Moisture_Percent
            if(Happy_DataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending savory")
                client.send(bytes('savory\n','utf-8'))
                #client.close()
                Happy_DataSent = 1
                Savory_DataSent = 0
                Thirsty_DataSent = 0

        if(Temperature>Temperature_max):
            if(TemperatureDataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending hot")
                client.send(bytes('hot\n','utf-8'))
                #client.close()
                TemperatureDataSent = 1
        elif(Temperature<Temperature_min):
            if(TemperatureDataSent == 0):
                #client.connect(('0.0.0.0', 8080))
                _LOGGER.info("Sending freeze")
                client.send(bytes('freeze\n','utf-8'))
                #client.close()
                TemperatureDataSent = 1
        else:
                TemperatureDataSent = 0
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
