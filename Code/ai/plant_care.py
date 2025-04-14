# This script contains a dictionary with plant care information for various houseplants.
# The dictionary includes details such as light, water, soil, temperature, and moisture requirements for each plant.
plant_care_data = {
    "Monstera deliciosa": {
        "common_name": "Fensterblatt",
        "light": {"min": 5000, "max": 20000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 7.0, "type": "humusreich"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Ficus benjamina": {
        "common_name": "Birkenfeige",
        "light": {"min": 3000, "max": 10000, "unit": "lux"},
        "water": {"min": 200, "max": 400, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.5, "type": "locker, durchlässig"},
        "temperature": {"min": 15, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Sansevieria trifasciata": {
        "common_name": "Bogenhanf",
        "light": {"min": 500, "max": 8000, "unit": "lux"},
        "water": {"min": 50, "max": 150, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 7.5, "type": "Kakteenerde"},
        "temperature": {"min": 15, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Zamioculcas zamiifolia": {
        "common_name": "Glücksfeder",
        "light": {"min": 300, "max": 5000, "unit": "lux"},
        "water": {"min": 75, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "durchlässig"},
        "temperature": {"min": 15, "max": 26, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Chlorophytum comosum": {
        "common_name": "Grünlilie",
        "light": {"min": 1000, "max": 8000, "unit": "lux"},
        "water": {"min": 100, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.5, "type": "Blumenerde"},
        "temperature": {"min": 10, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Dracaena marginata": {
        "common_name": "Drachenbaum",
        "light": {"min": 1500, "max": 10000, "unit": "lux"},
        "water": {"min": 100, "max": 250, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 6.8, "type": "leicht sauer"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Dieffenbachia seguine": {
        "common_name": "Dieffenbachie",
        "light": {"min": 800, "max": 5000, "unit": "lux"},
        "water": {"min": 150, "max": 350, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "humos"},
        "temperature": {"min": 18, "max": 26, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Spathiphyllum wallisii": {
        "common_name": "Einblatt",
        "light": {"min": 500, "max": 4000, "unit": "lux"},
        "water": {"min": 200, "max": 400, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Anthurium andraeanum": {
        "common_name": "Flamingoblume",
        "light": {"min": 1500, "max": 6000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 5.0, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 18, "max": 28, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Calathea orbifolia": {
        "common_name": "Korbmarante",
        "light": {"min": 500, "max": 2000, "unit": "lux"},
        "water": {"min": 200, "max": 400, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer, torfig"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Aloe vera": {
        "common_name": "Echte Aloe",
        "light": {"min": 2000, "max": 6000, "unit": "lux"},
        "water": {"min": 50, "max": 150, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Kaktuserde"},
        "temperature": {"min": 15, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Pothos": {
        "common_name": "Efeutute",
        "light": {"min": 500, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 30, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Philodendron": {
        "common_name": "Philodendron",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 7.0, "type": "torfhaltig"},
        "temperature": {"min": 18, "max": 28, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Ficus elastica": {
        "common_name": "Gummibaum",
        "light": {"min": 2000, "max": 8000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 16, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Codiaeum variegatum": {
        "common_name": "Kroton",
        "light": {"min": 3000, "max": 7000, "unit": "lux"},
        "water": {"min": 100, "max": 250, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "humusreich"},
        "temperature": {"min": 20, "max": 30, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Hoya carnosa": {
        "common_name": "Wachsblume",
        "light": {"min": 1500, "max": 6000, "unit": "lux"},
        "water": {"min": 50, "max": 150, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 15, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Spathiphyllum": {
        "common_name": "Einblatt",
        "light": {"min": 500, "max": 4000, "unit": "lux"},
        "water": {"min": 200, "max": 400, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Neoregalia": {
        "common_name": "Bromelie",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 20, "max": 30, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Pilea peperomioides": {
        "common_name": "UFO Pflanze",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Begonia": {
        "common_name": "Begonie",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Cactus": {
        "common_name": "Kaktus",
        "light": {"min": 3000, "max": 10000, "unit": "lux"},
        "water": {"min": 10, "max": 50, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.5, "type": "Kaktuserde"},
        "temperature": {"min": 15, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Crassula ovata": {
        "common_name": "Geldbaum",
        "light": {"min": 2000, "max": 8000, "unit": "lux"},
        "water": {"min": 50, "max": 100, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Kaktuserde"},
        "temperature": {"min": 15, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Tradescantia": {
        "common_name": "Tradescantia",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 15, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Zamioculcas zamiifolia": {
        "common_name": "Glücksfeder",
        "light": {"min": 300, "max": 5000, "unit": "lux"},
        "water": {"min": 75, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "durchlässig"},
        "temperature": {"min": 15, "max": 26, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Orchidee": {
        "common_name": "Orchidee",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 50, "max": 150, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "orchideenerde"},
        "temperature": {"min": 20, "max": 25, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Kalanchoe": {
        "common_name": "Kalanchoe",
        "light": {"min": 2000, "max": 8000, "unit": "lux"},
        "water": {"min": 50, "max": 150, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Kaktuserde"},
        "temperature": {"min": 15, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Asplenium": {
        "common_name": "Schwertfarn",
        "light": {"min": 500, "max": 3000, "unit": "lux"},
        "water": {"min": 100, "max": 250, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 7.0, "type": "torfhaltig"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Ficus lyrata": {
        "common_name": "Geigenfeige",
        "light": {"min": 2000, "max": 8000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 28, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Alocasia": {
        "common_name": "Alokasie",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 20, "max": 28, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Cycad": {
        "common_name": "Zyka",
        "light": {"min": 2000, "max": 6000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 30, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Hibiscus": {
        "common_name": "Hibiskus",
        "light": {"min": 2000, "max": 8000, "unit": "lux"},
        "water": {"min": 150, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 30, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Bamboo palm": {
        "common_name": "Bambuspalme",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Dracaena fragrans": {
        "common_name": "Duftdracaena",
        "light": {"min": 1500, "max": 6000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Parlor palm": {
        "common_name": "Zimmerpalme",
        "light": {"min": 500, "max": 3000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Chinese evergreen": {
        "common_name": "Aglaonema",
        "light": {"min": 500, "max": 3000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Money tree": {
        "common_name": "Geldbaum",
        "light": {"min": 2000, "max": 6000, "unit": "lux"},
        "water": {"min": 100, "max": 300, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Kaktuserde"},
        "temperature": {"min": 18, "max": 30, "unit": "°C"},
        "moisture": {"min": 10, "max": 30, "unit": "%"}
    },
    "Oxalis": {
        "common_name": "Sauerklee",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 15, "max": 25, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Kentiapalme": {
        "common_name": "Kentiapalme",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Fatsia japonica": {
        "common_name": "Japanische Aralie",
        "light": {"min": 500, "max": 3000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "torfhaltig"},
        "temperature": {"min": 15, "max": 25, "unit": "°C"},
        "moisture": {"min": 70, "max": 100, "unit": "%"}
    },
    "Schefflera": {
        "common_name": "Schefflera",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Bromelia": {
        "common_name": "Bromelie",
        "light": {"min": 1000, "max": 5000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
        "temperature": {"min": 20, "max": 30, "unit": "°C"},
        "moisture": {"min": 60, "max": 90, "unit": "%"}
    },
    "Arecapalme": {
        "common_name": "Arecapalme",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 24, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    },
    "Pachira aquatica": {
        "common_name": "Pachira",
        "light": {"min": 1000, "max": 4000, "unit": "lux"},
        "water": {"min": 100, "max": 200, "unit": "ml/week"},
        "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
        "temperature": {"min": 18, "max": 30, "unit": "°C"},
        "moisture": {"min": 40, "max": 70, "unit": "%"}
    }
}

def get_plant_info(latin_name):
    """
    Retrieve plant care information based on the Latin name.
    Args:
        latin_name (str): The Latin name of the plant.
    Returns:
        dict: A dictionary containing care information for the plant.
    """
    plant_info = plant_care_data.get(latin_name)
    if plant_info:
        return plant_info
    else:
        return f"No information found for the plant {latin_name}."