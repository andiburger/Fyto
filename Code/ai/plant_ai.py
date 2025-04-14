import requests
import pprint

def identify_plant(image_path, api_key):
    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={api_key}"

    files = {
        'images': open(image_path, 'rb')
    }

    data = {
        'organs': 'leaf'  # You can adjust this to 'flower', 'fruit', etc.
    }

    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        result = response.json()
        pprint.pp(result)
        if result["results"]:
            plant_info = result["results"][0]
            return {
                "name": plant_info["species"]["scientificName"],
                "common_names": plant_info["species"]["commonNames"],
                "confidence": plant_info["score"]
            }
        else:
            return {"error": "plant not found"}
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}
