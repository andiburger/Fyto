import requests
import pprint
import logging
from plant_care import PlantCare

_LOGGER = logging.getLogger(__name__)

def identify_plant(file_path, api_key):
    """Identify a plant using the PlantNet API.
    Args:
        file_path (str): Path to the image file.
        api_key (str): Your PlantNet API key.
    Returns:
        dict: A dictionary containing the plant's scientific name, common names, and confidence score.
    """
    # Ensure you have the correct API endpoint and parameters
    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={api_key}"

    files = {
        'images': open(file_path, 'rb')
    }

    data = {
        'organs': 'leaf'  # You can adjust this to 'flower', 'fruit', etc.
    }

    myPlantDatabase = PlantCare()

    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        pprint.pp(result)
        if result["results"]:
            plant_info = result["results"][0]
            # Extracting the best match information
            detailed_plant_info, confidence = myPlantDatabase.get_plant_info(plant_info["species"]["scientificName"])
            if not detailed_plant_info:
                _LOGGER.error("No exact information found for the plant.")
            else:
                _LOGGER.info(f"Best match: {detailed_plant_info['common_name']} with confidence {confidence}")
            return {
                "scientific_name": result["bestMatch"],
                "common_names": ', '.join(plant_info["species"]["commonNames"]),
                "confidence": plant_info["score"],
                "detailed_info": detailed_plant_info,
                "confidence_level": confidence
            }
        else:
            return {"error": "plant not found"}
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}
