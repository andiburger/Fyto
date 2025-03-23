import board
import busio
import time
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1115 as ADS # type: ignore
from adafruit_ads1x15.analog_in import AnalogIn # type: ignore

ads = ADS.ADS1115(i2c)
# Analog input channels may differ based on the connection
# For example, if the moisture sensor is connected to A0, then the channel should be ADS.P0
Moisture_channel = AnalogIn(ads, ADS.P1)
LDR_channel = AnalogIn(ads, ADS.P2)
LM35_channel = AnalogIn(ads, ADS.P3)

# Temperaturberechnung: 10 mV pro °C für den LM35
def read_temperature():
    # Lese den Rohwert vom ADC
    raw_value = ads.readADC(0, gain=1)  # gain=1 für ±4.096V Referenz
    voltage = raw_value * (4.096 / 32768)  # Berechne die Spannung basierend auf dem Rohwert
    temperature = voltage * 100  # LM35 gibt 10mV/°C aus, also multiplizieren mit 100
    return temperature


while True:
   print("Moisture: "+ str(Moisture_channel.value))
   print("Light Intensity:" + str(LDR_channel.value))
   print("Temperature:" + str(LM35_channel.value))
   temp = read_temperature()
   print(f"Temperature: {temp:.2f} °C")
   time.sleep(1)

