import difflib


class PlantCare:
    def __init__(self):
        # The dictionary includes details such as light, water, soil, temperature, and moisture requirements for each plant.
        self.plant_care_data = {
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
            "Chlorophytum comosum": { # Consolidated 'Chlorophytum comosum 'Variegatum'' here
                "common_name": "Grünlilie", # Could add '(inkl. Variegata)' if desired
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
            "Spathiphyllum wallisii": { # Consolidated 'Spathiphyllum' here
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
            "Epipremnum aureum": { # Consolidated 'Pothos' here
                "common_name": "Goldene Efeutute", # Often called Pothos
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
            "Neoregalia": { # Keeping as a specific Bromeliad genus
                "common_name": "Bromelie",
                "light": {"min": 1000, "max": 5000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"}, # Water in the central cup
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
            "Cactus": { # Keeping as a general category, could be more specific if needed
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
            "Orchidee": { # Keeping as a general category, could be more specific if needed
                "common_name": "Orchidee",
                "light": {"min": 1000, "max": 5000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "orchideenerde"},
                "temperature": {"min": 20, "max": 25, "unit": "°C"},
                "moisture": {"min": 60, "max": 90, "unit": "%"}
            },
            "Kalanchoe": { # Keeping as a general category, could be more specific if needed
                "common_name": "Kalanchoe",
                "light": {"min": 2000, "max": 8000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Kaktuserde"},
                "temperature": {"min": 15, "max": 30, "unit": "°C"},
                "moisture": {"min": 10, "max": 30, "unit": "%"}
            },
            "Asplenium": { # Keeping as a genus, could be more specific (e.g., Asplenium nidus)
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
            "Alocasia": { # Keeping as a genus
                "common_name": "Alokasie",
                "light": {"min": 1000, "max": 5000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
                "temperature": {"min": 20, "max": 28, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Cycad": { # Keeping as a general category/genus
                "common_name": "Zyka",
                "light": {"min": 2000, "max": 6000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 30, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Hibiscus": { # Keeping as a genus
                "common_name": "Hibiskus",
                "light": {"min": 2000, "max": 8000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 30, "unit": "°C"},
                "moisture": {"min": 60, "max": 90, "unit": "%"}
            },
            "Bamboo palm": { # Keeping as a common name category, could be more specific
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
            "Parlor palm": { # Keeping as a common name category, could be more specific
                "common_name": "Zimmerpalme",
                "light": {"min": 500, "max": 3000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Aglaonema commutatum": { # Consolidated 'Chinese evergreen' here
                "common_name": "Kolbenfaden", # Also Chinese evergreen
                "light": {"min": 800, "max": 3000, "unit": "lux"},
                "water": {"min": 100, "max": 250, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "humos, gut durchlässig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Oxalis": { # Keeping as a genus
                "common_name": "Sauerklee",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
                "temperature": {"min": 15, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Kentiapalme": { # Keeping as a common name category, could be more specific
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
            "Schefflera": { # Keeping as a genus
                "common_name": "Schefflera",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Bromelia": { # Keeping as a genus
                "common_name": "Bromelie",
                "light": {"min": 1000, "max": 5000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"}, # Water in the central cup
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
                "temperature": {"min": 20, "max": 30, "unit": "°C"},
                "moisture": {"min": 60, "max": 90, "unit": "%"}
            },
            "Arecapalme": { # Keeping as a common name category, could be more specific
                "common_name": "Arecapalme",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Pachira aquatica": { # Consolidated 'Money tree' here
                "common_name": "Pachira", # Also Money tree
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Blumenerde"},
                "temperature": {"min": 18, "max": 30, "unit": "°C"},
                "moisture": {"min": 40, "max": 70, "unit": "%"}
            },
            "Maranta leuconeura": {
                "common_name": "Gebetspflanze",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.0, "type": "leicht sauer, torfhaltig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 60, "max": 90, "unit": "%"}
            },
            "Nephrolepis exaltata": {
                "common_name": "Boston Farn",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 200, "max": 400, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Saintpaulia ionantha": {
                "common_name": "Usambaraveilchen",
                "light": {"min": 800, "max": 2000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "leicht sauer, gut durchlässig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Aspidistra elatior": {
                "common_name": "Schusterpalme",
                "light": {"min": 300, "max": 2000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.5, "type": "durchlässig"},
                "temperature": {"min": 10, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Clivia miniata": {
                "common_name": "Klivi",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "humos, gut durchlässig"},
                "temperature": {"min": 10, "max": 20, "unit": "°C"}, # Lower temp for flowering
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Schlumbergera": {
                "common_name": "Weihnachtskaktus",
                "light": {"min": 1000, "max": 3000, "unit": "lux"},
                "water": {"min": 50, "max": 100, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.0, "type": "leicht sauer, durchlässig"},
                "temperature": {"min": 15, "max": 23, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Peperomia obtusifolia": {
                "common_name": "Zwergpfeffer",
                "light": {"min": 1000, "max": 3000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "durchlässig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Streptocarpus": {
                "common_name": "Drehfrucht",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "torfhaltig, gut durchlässig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 50, "max": 80, "unit": "%"}
            },
            "Columnea": {
                "common_name": "Goldfischpflanze",
                "light": {"min": 1000, "max": 3000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig, locker"},
                "temperature": {"min": 18, "max": 26, "unit": "°C"},
                "moisture": {"min": 60, "max": 80, "unit": "%"}
            },
            "Episcia": {
                "common_name": "Flammenveilchen",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "torfhaltig, gut durchlässig"},
                "temperature": {"min": 20, "max": 28, "unit": "°C"},
                "moisture": {"min": 70, "max": 90, "unit": "%"}
            },
            "Nematanthus": {
                "common_name": "Küsschenpflanze",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 50, "max": 150, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "torfhaltig, locker"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 50, "max": 70, "unit": "%"}
            },
            "Aeschynanthus": { # Keeping as a genus
                "common_name": "Blushrüssel",
                "light": {"min": 1500, "max": 5000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "torfhaltig, gut durchlässig"},
                "temperature": {"min": 20, "max": 28, "unit": "°C"},
                "moisture": {"min": 60, "max": 80, "unit": "%"}
            },
            "Ctenanthe oppenheimiana": {
                "common_name": "Gebetspflanzen-Verwandte",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer, torfig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Stromanthe sanguinea": {
                "common_name": "Gebetspflanzen-Verwandte",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer, torfig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Calathea lancifolia": {
                "common_name": "Lanzen-Korbmarante",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 5.5, "ph_max": 6.5, "type": "leicht sauer, torfig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Fittonia albivenis": {
                "common_name": "Fittonien",
                "light": {"min": 500, "max": 2000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "torfhaltig, feucht"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 70, "max": 100, "unit": "%"}
            },
            "Hypoestes phyllostachya": {
                "common_name": "Punktblatt",
                "light": {"min": 1000, "max": 4000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "humos, gut durchlässig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Stephanotis floribunda": {
                "common_name": "Kranzschlinge",
                "light": {"min": 2000, "max": 6000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "leicht sauer, durchlässig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 60, "max": 80, "unit": "%"}
            },
            "Beaucarnea recurvata": {
                "common_name": "Elefantenfuß",
                "light": {"min": 3000, "max": 10000, "unit": "lux"},
                "water": {"min": 50, "max": 100, "unit": "ml/week"}, # Stores water in caudex
                "soil": {"ph_min": 6.0, "ph_max": 7.5, "type": "Kaktuserde"},
                "temperature": {"min": 10, "max": 25, "unit": "°C"},
                "moisture": {"min": 10, "max": 30, "unit": "%"}
            },
            "Haworthia fasciata": {
                "common_name": "Zebra-Haworthie",
                "light": {"min": 2000, "max": 5000, "unit": "lux"},
                "water": {"min": 30, "max": 80, "unit": "ml/week"}, # Succulent
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Sukkulentenerde"},
                "temperature": {"min": 15, "max": 25, "unit": "°C"},
                "moisture": {"min": 10, "max": 30, "unit": "%"}
            },
            "Echeveria": { # Keeping as a genus
                "common_name": "Echeverie",
                "light": {"min": 3000, "max": 8000, "unit": "lux"},
                "water": {"min": 30, "max": 80, "unit": "ml/week"}, # Succulent
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Sukkulentenerde"},
                "temperature": {"min": 18, "max": 28, "unit": "°C"},
                "moisture": {"min": 10, "max": 30, "unit": "%"}
            },
            "Sedum morganianum": {
                "common_name": "Affenschwanz",
                "light": {"min": 3000, "max": 8000, "unit": "lux"},
                "water": {"min": 30, "max": 80, "unit": "ml/week"}, # Succulent
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Sukkulentenerde"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 10, "max": 30, "unit": "%"}
            },
            "Lithops": {
                "common_name": "Lebende Steine",
                "light": {"min": 5000, "max": 10000, "unit": "lux"},
                "water": {"min": 5, "max": 20, "unit": "ml/week"}, # Very low water
                "soil": {"ph_min": 7.0, "ph_max": 8.0, "type": "sehr durchlässig, mineralisch"},
                "temperature": {"min": 20, "max": 30, "unit": "°C"},
                "moisture": {"min": 0, "max": 10, "unit": "%"} # Very low moisture
            },
            "Mimosa pudica": {
                "common_name": "Mimose / Rühr-mich-nicht-an",
                "light": {"min": 2000, "max": 5000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "locker, feucht"},
                "temperature": {"min": 20, "max": 25, "unit": "°C"},
                "moisture": {"min": 50, "max": 70, "unit": "%"}
            },
            "Coffea arabica": {
                "common_name": "Kaffeepflanze",
                "light": {"min": 1500, "max": 4000, "unit": "lux"},
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 6.5, "type": "leicht sauer, torfhaltig"},
                "temperature": {"min": 18, "max": 24, "unit": "°C"},
                "moisture": {"min": 50, "max": 70, "unit": "%"}
            },
            "Murraya paniculata": {
                "common_name": "Orangenraute / Duftjasmin",
                "light": {"min": 2000, "max": 6000, "unit": "lux"},
                "water": {"min": 100, "max": 200, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "gut durchlässig"},
                "temperature": {"min": 18, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            },
            "Citrus × limon": {
                "common_name": "Zitronenbaum (Zimmer)",
                "light": {"min": 4000, "max": 10000, "unit": "lux"}, # Needs lots of light
                "water": {"min": 150, "max": 300, "unit": "ml/week"},
                "soil": {"ph_min": 6.0, "ph_max": 7.0, "type": "Zitruspflanzenerde"},
                "temperature": {"min": 10, "max": 25, "unit": "°C"},
                "moisture": {"min": 40, "max": 60, "unit": "%"}
            }
        }
        return

    def get_plant_info(self, latin_name):
        """
        Retrieve plant care information based on the exact Latin name.
        Args:
            latin_name (str): The exact Latin name of the plant.
        Returns:
            dict or str: A dictionary containing care information for the plant
                        or a message if not found.
        """
        plant_info = self.plant_care_data.get(latin_name)
        if plant_info:
            return plant_info
        else:
            return f"No exact information found for the plant {latin_name}."


    def search_plant_fuzzy(self, query, min_confidence=0.6):
        """
        Search for plant care information using a potentially similar Latin name,
        returning the best match data and a confidence score.

        Args:
            plant_data_dict (dict): The dictionary containing plant care data.
            query (str): The Latin name to search for (can be partial or similar).
            min_confidence (float): The minimum similarity score (0.0 to 1.0) to consider a match valid.

        Returns:
            tuple: (plant_info, confidence)
                plant_info is the dictionary of plant data for the best match, or None if no valid match.
                confidence is a float (0.0 to 1.0) indicating the similarity of the best match to the query.
                Returns (None, 0.0) if no match meets the min_confidence threshold.
        """
        best_match_data = None
        highest_confidence = 0.0
        best_match_name = None

        # Normalize the query for case-insensitive matching
        query_lower = query.lower()

        # Iterate through all possible plant names in the dictionary keys
        for latin_name in self.plant_care_data.keys():
            # Calculate the similarity ratio between the query and the current plant name
            matcher = difflib.SequenceMatcher(None, query_lower, latin_name.lower())
            similarity_ratio = matcher.ratio()

            # Check if this is the best match found so far
            if similarity_ratio > highest_confidence:
                highest_confidence = similarity_ratio
                best_match_name = latin_name
                best_match_data = self.plant_care_data[latin_name]

        # If the highest confidence is below the minimum required confidence, return no match
        if highest_confidence < min_confidence:
            return None, 0.0
        else:
            # Return the data for the best match and its confidence level
            return best_match_data, highest_confidence
