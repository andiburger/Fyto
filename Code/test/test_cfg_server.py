import pytest
import sys
import os
import requests
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_cfg_server_empty_config(): 
    url = 'http://127.0.0.1:5000/get_config'
    response = requests.get(url)
    if response.status_code == 200:
        config_data = response.json() 
        print(config_data)
    else:
        print(f"Error: {response.status_code}")
    assert config_data == {
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

def test_mqtt_cfg_available():
    url = 'http://127.0.0.1:5000/get_config'
    response = requests.get(url)
    if response.status_code == 200:
        config_data = response.json() 
        print(config_data['MQTT Host'])
    else:
        print(f"Error: {response.status_code}")
    assert config_data['MQTT Host'] != "" and config_data['MQTT Topic'] != "" and config_data['MQTT Port'] != ""
     



if __name__ == '__main__':
    test_cfg_server_empty_config()
    test_mqtt_cfg_available()