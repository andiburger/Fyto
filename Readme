# Smart Plant Pot

todo

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

