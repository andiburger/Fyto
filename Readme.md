# Smart Plant Pot

Inspired by [Fyto Project](https://www.hackster.io/coderscafe/fyto-turn-your-plant-into-pet-1373d5#code)

## Hardware components
- Raspberry Pi Zero 2 W
- ADS1115 ADC Module 16Bit 4 channels for Raspberry Pi
- Soil Moisture Sensor Hygrometer Module V1.2
- DS18B20 digital temperature sensor
- LDR-Lichtsensor resistiv
- Power Distributor Terminal Block 2x12

## Wiring
![Wiring with RPI Zero 2 w](Code/img/wiring_smart_pot_bb.png)

## Installation & Setup

### Prerequisites
- Python 3.11 or later
- Virtual environment (recommended)
- Dependencies from `requirements.txt`

### Installation
1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create & activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### **Start the Main Program**
The `main.py` script starts the configuration server and sensor system as subprocesses.
```sh
python main.py
```

## **Configure Smart Pot via Configuration Server
Open a web browser and connect to the configuration server with the following address: `https://PI-ZERO-IP-ADDR:5000`

![Screenshot of configuration server](Code/img/config_server.png)

Set the parameter as shown in the screenshot above. MQTT User and Password are optional.
The following parameter can be used as default for light intensity, temperature and moisture:
- Light intensity min: 20
- Light intensity max: 20

- Temperature min: 22
- Temperature max: 30

- Moisture min: 10
- Moisture max: 90

## API Endpoints (config_server.py)
| Method  | Endpoint       | Description |
|---------|---------------|-------------|
| `GET`   | `/config`     | Retrieve configuration settings |
| `POST`  | `/config`     | Set configuration settings |

### Configurable Parameters:
The following parameters can be set via the `/config` endpoint:
- `moisture` (int): The soil moisture level at which watering should be triggered.
- `temperature` (float): Maximum temperature before triggering an alert.
- `light` (int): Minimum required light intensity for the plant.


## Troubleshooting
- If you encounter a `Permission denied` error, try running the script with `sudo` or changing the port number.
- Ensure that `pip install -r requirements.txt` has been executed.

## License
This project is licensed under the MIT License.

