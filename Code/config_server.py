from flask import Flask, request, jsonify, render_template
from ai.plant_ai import identify_plant
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration data
config_data = {
    "MQTT Host": "",
    "MQTT Port": "1883",
    "MQTT Topic": "",
    "MQTT Username": "",
    "MQTT Password": "",
    "Light Intensity min": "",
    "Light Intensity max": "",
    "Temperature min": "",
    "Temperature max": "",
    "Moisture min": "",
    "Moisture max": ""
}
# Configuration page
@app.route('/')
def index():
    """Render the configuration page."""
    return render_template('config.html', config=config_data)
# API to set configuration
@app.route('/set_config', methods=['POST'])
def set_config():
    """Set the configuration data."""
    global config_data
    config_data.update(request.form)
    return jsonify({"message": "Configuration saved successfully"})
# API to get configuration
@app.route('/get_config', methods=['GET'])
def get_config():
    """Get the current configuration data."""
    return jsonify(config_data)

@app.route("/plant_identification")
def plant_identification():
    """Render the plant identification page."""
    return render_template("plant_identification.html")

@app.route('/upload_image', methods=['POST'])
def upload_image():
    """Handle image upload and plant identification."""
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    api_key = request.form.get("api_key", type=str)

    if file.filename == '':
        return "No selected file", 400

    # Upload-Pfad erstellen
    upload_folder = os.path.join(os.path.dirname(__file__), "static", "uploads")
    os.makedirs(upload_folder, exist_ok=True)

    # Datei speichern
    filename = secure_filename(file.filename)  # falls nicht schon vorhanden, import: from werkzeug.utils import secure_filename
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    # relative URL für Anzeige im Template
    image_url = f"/static/uploads/{filename}"

    # Bild analysieren
    result = identify_plant(file_path=file_path, api_key=api_key)

    # Template anzeigen mit Ergebnis und Bild
    return render_template("plant_identification.html", plant_data=result, api_key=api_key, image_url=image_url)


# Run the server
if __name__ == '__main__':
    """Run the Flask application."""
    app.run(debug=True)
