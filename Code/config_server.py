from flask import Flask, request, jsonify, render_template
from ai.plant_ai import identify_plant

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
    return render_template('config.html', config=config_data)
# API to set configuration
@app.route('/set_config', methods=['POST'])
def set_config():
    global config_data
    config_data.update(request.form)
    return jsonify({"message": "Configuration saved successfully"})
# API to get configuration
@app.route('/get_config', methods=['GET'])
def get_config():
    return jsonify(config_data)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image_path = request.form.get('image')
    return identify_plant(image_path,None)

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
