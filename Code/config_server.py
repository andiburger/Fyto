from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Speichert die Konfiguration im Arbeitsspeicher
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

@app.route('/')
def index():
    return render_template('config.html', config=config_data)

@app.route('/set_config', methods=['POST'])
def set_config():
    global config_data
    config_data.update(request.form)
    return jsonify({"message": "Configuration saved successfully"})

@app.route('/get_config', methods=['GET'])
def get_config():
    return jsonify(config_data)

if __name__ == '__main__':
    app.run(debug=True)
