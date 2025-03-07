import time
import socket
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

from paho.mqtt import client as mqtt_client
import random
import logging
import json

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
Moisture_channel = AnalogIn(ads, ADS.P2)
LDR_channel = AnalogIn(ads, ADS.P3)
LM35_channel = AnalogIn(ads, ADS.P1)

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

# constants for mqtt
broker = '192.168.178.160'
port = 1883
topic = "smart_pot/data"
client_id = f'smart_pot-{random.randint(0, 1000)}'
# username = 'YOUR_USERNAME'
# password = 'YOUR_PASSWORD'
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


_LOGGER = logging.getLogger(__name__)

# Map function
def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
    # For paho-mqtt 2.0.0, you need to add the properties parameter.
    # def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)

    # For paho-mqtt 2.0.0, you need to set callback_api_version.
    # client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)

    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_disconnect(client, userdata, rc):
    _LOGGER.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        _LOGGER.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)

        try:
            client.reconnect()
            _LOGGER.info("Reconnected successfully!")
            return
        except Exception as err:
            _LOGGER.error("%s. Reconnect failed. Retrying...", err)

        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    _LOGGER.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)


#Setup Client for communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 1013))

mqtt_client = connect_mqtt()
mqtt_client.on_disconnect = on_disconnect
mqtt_client.loop_start()


while True:
    
    # Read the specified ADC channels using the previously set gain value.
    LDR_Value = LDR_channel.value
    LDR_Percent = _map(LDR_Value, 22500, 50, 0, 100)
    Moisture_Value = Moisture_channel.value
    Moisture_Percent = _map(Moisture_Value, 31000, 15500, 0, 100)
    ads_ch0 = LM35_channel.value
    ads_Voltage_ch0 = ads_ch0 * ads_bit_Voltage
    Temperature = int(ads_Voltage_ch0 / lm35_constant)
    print("Temperature = ", Temperature)
    print("Light Intensity = ", LDR_Percent)
    print("Moisture % = ", Moisture_Percent)
    MQTT_MSG=json.dumps({"Temperature":Temperature,"Light Intensity":LDR_Percent,"Moisture %":Moisture_Percent})
    result = mqtt_client.publish(topic, MQTT_MSG)
    status = result[0]
    if status == 0:
        _LOGGER.info(f"Send `{MQTT_MSG}` to topic `{topic}`")
    else:      
        _LOGGER.error(f"Failed to send message to topic {topic}")
    if (LDR_Percent < 20):
        if(LowIn_DataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('sleep','utf-8'))
            #client.close()
            HighIn_DataSent = 0
            LowIn_DataSent = 1
    elif (LDR_Percent > 20):
        if(HighIn_DataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('happy','utf-8'))
            #client.close()
            HighIn_DataSent = 1
            LowIn_DataSent = 0
        
    if (Moisture_Percent < 10):
        Moisture_Recent = Moisture_Percent
        if(Thirsty_DataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('thirs','utf-8'))
            #client.close()
            Thirsty_DataSent = 1
            Savory_DataSent = 0
            Happy_DataSent = 0
    elif (Moisture_Percent>10 and Moisture_Recent < Moisture_Percent and Moisture_Percent < 90):
        Moisture_Recent = Moisture_Percent
        if(Savory_DataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('savor','utf-8'))
            #client.close()
            Savory_DataSent = 1
            Thirsty_DataSent = 0
            Happy_DataSent = 0
    elif (Moisture_Percent > 90):
        Moisture_Recent = Moisture_Percent
        if(Happy_DataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('savor','utf-8'))
            #client.close()
            Happy_DataSent = 1
            Savory_DataSent = 0
            Thirsty_DataSent = 0

    if(Temperature>30):
        if(TemperatureDataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('hotty','utf-8'))
            #client.close()
            TemperatureDataSent = 1
    elif(Temperature<22):
        if(TemperatureDataSent == 0):
            #client.connect(('0.0.0.0', 8080))
            client.send(bytes('freez','utf-8'))
            #client.close()
            TemperatureDataSent = 1
    else:
            TemperatureDataSent = 0
