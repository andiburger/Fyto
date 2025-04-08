from datetime import datetime, timedelta
from astral.geocoder import database, lookup
from astral.sun import sun
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger(__name__)

def get_location(city_name):
    try:
        location = lookup(city_name, database())
        return location
    except KeyError:
        _LOGGER.error(f"Error: The city '{city_name}' was not found.")
        return None

def get_sun_times(city):
    s = sun(city.observer, date=datetime.now(), tzinfo=city.timezone)
    # Apply 2-hour offset
    sunrise = (s["sunrise"] + timedelta(hours=2)).time()
    sunset = (s["sunset"] + timedelta(hours=2)).time()
    return sunrise, sunset