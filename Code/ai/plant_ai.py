import requests
import pprint

def identify_plant(file_path, api_key):
    url = f"https://my-api.plantnet.org/v2/identify/all?api-key={api_key}"

    files = {
        'images': open(file_path, 'rb')
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
                "scientific_name": result["bestMatch"],
                "common_names": ', '.join(plant_info["species"]["commonNames"]),
                "confidence": plant_info["score"]
            }
        else:
            return {"error": "plant not found"}
    else:
        return {"error": f"Error: {response.status_code} - {response.text}"}
