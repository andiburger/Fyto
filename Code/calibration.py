import board
import busio
import time
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)
Moisture_channel = AnalogIn(ads, ADS.P1)
LDR_channel = AnalogIn(ads, ADS.P2)
LM35_channel = AnalogIn(ads, ADS.P3)
while True:
   print(Moisture_channel.value)
   print(LDR_channel.value)
   print(LM35_channel.value)
   time.sleep(0.1)

