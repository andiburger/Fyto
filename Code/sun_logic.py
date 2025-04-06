from datetime import datetime
from astral.geocoder import database, lookup
from astral.sun import sun

def get_location(city_name):
    try:
        location = lookup(city_name, database())
        return location
    except KeyError:
        print(f"Error: The city '{city_name}' was not found.")
        return None

def get_sun_times(city):
    s = sun(city.observer, date=datetime.now())
    sunrise = s["sunrise"].time()
    sunset = s["sunset"].time()
    return sunrise, sunset