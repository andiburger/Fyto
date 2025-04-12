# sensor_read.py
import logging
import busio
import board
import adafruit_ads1x15.ads1115 as ADS # type: ignore
from adafruit_ads1x15.analog_in import AnalogIn # type: ignore
from w1thermsensor import W1ThermSensor # type: ignore
import RPi.GPIO as GPIO # type: ignore

 # Set up the backlight pin
BACKLIGHT_PIN = 18

class Sensor:
    """Sensor class to read data from various sensors."""
   

    def __init__(self):
        """Initialize the sensor class."""
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self._LOGGER = logging.getLogger(__name__)
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        # Analog input channels may differ based on the connection
        # use calibration.py to find the correct channel
        self.Moisture_channel = AnalogIn(self.ads, ADS.P1)
        self.LDR_channel = AnalogIn(self.ads, ADS.P2)
        #LM35_channel = AnalogIn(ads, ADS.P3 # necessary for LM35

        # set GPIO mode
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BACKLIGHT_PIN, GPIO.OUT)

        self.temp_sensor = W1ThermSensor()

        self.ADC_16BIT_MAX = 65536
        self.lm35_constant = 10.0/1000
        self.ads_InputRange = 4.096 #For Gain = 1; Otherwise change accordingly
        self.ads_bit_Voltage = (self.ads_InputRange * 2) / (self.ADC_16BIT_MAX - 1)
        self._LOGGER.info("Sensor class initialized.")
        return
    
    def _map(self, x, in_min, in_max, out_min, out_max):
        """Map a value from one range to another.
        Args:
            x (int): The value to map.
            in_min (int): The minimum of the input range.
            in_max (int): The maximum of the input range.
            out_min (int): The minimum of the output range.
            out_max (int): The maximum of the output range.
        Returns:
            int: The mapped value.
        """
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    def read_sensor_data(self):
        """Read data from the sensors and return it as a tuple.
        Returns:
            tuple: A tuple containing temperature, light intensity (LDR), and moisture level.
        """
        ldr_val = self.LDR_channel.value
        ldr = self._map(ldr_val, 22500, 50, 0, 100)

        moisture_val = self.Moisture_channel.value
        moisture = self._map(moisture_val, 31000, 15500, 0, 100)

        temp = self.temp_sensor.get_temperature()
        self._LOGGER.debug(f"Temperature: {temp} °C")
        self._LOGGER.debug(f"LDR Value: {ldr_val} -> LDR Percent: {ldr}")
        self._LOGGER.debug(f"Moisture Value: {moisture_val} -> Moisture Percent: {moisture}")
        return temp, ldr, moisture