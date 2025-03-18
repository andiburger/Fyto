import board
import busio
import time
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)
# Analog input channels may differ based on the connection
# For example, if the moisture sensor is connected to A0, then the channel should be ADS.P0
Moisture_channel = AnalogIn(ads, ADS.P1)
LDR_channel = AnalogIn(ads, ADS.P2)
LM35_channel = AnalogIn(ads, ADS.P3)
while True:
   print("Moisture: "+ Moisture_channel.value)
   print("Light Intensity:" + LDR_channel.value)
   print("Temperature:" + LM35_channel.value)
   time.sleep(1)

