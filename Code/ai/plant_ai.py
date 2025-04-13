import requests
import base64

def identify_plant(image_path):
    # Öffne das Bild und konvertiere es zu Base64
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode()

    # API-Endpunkt und Dein API-Key
    url = "https://api.plantnet.org/v2/identify/all"
    headers = {
        "Api-Key": "DEIN_API_KEY",
        "Content-Type": "application/json"
    }

    # Payload mit dem Bild
    payload = {
        "organs": ["flower", "leaf", "fruit", "stem", "seed"],  # Welche Teile der Pflanze analysiert werden sollen
        "images": [img_base64]
    }

    # Anfrage an die API
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Erfolgreiche Antwort
        data = response.json()
        if data["results"]:
            plant_info = data["results"][0]
            return {
                "name": plant_info["species"]["scientificName"],
                "common_names": plant_info["species"]["commonNames"],
                "confidence": plant_info["species"]["confidence"],
                "url": plant_info["species"]["url"]
            }
        else:
            return {"error": "plant not found"}
    else:
        return {"error": f"Error: {response.status_code}"}

# Beispiel für die Verwendung
plant_details = identify_plant("path_to_your_plant_image.jpg")
print(plant_details)