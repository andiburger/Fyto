import os
import sys 
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
import socket
import requests
import json
import subprocess
from threading import Thread
import time


# path to sensors script
script_path = 'sensors.py'
# path to config server script
config_server_path = 'config_server'
# global variable to store config data
config_data = {}

cfg_server_process = None
sensor_server_process = None

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
directory = os.getcwd()

#Server For Data Reception
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1013))
server.listen(2)

doInterrupt = 0
showOn = 0




def show(emotion):
    global doInterrupt, showOn, disp
    try:
        disp = LCD_2inch.LCD_2inch(spi=SPI.SpiDev(bus, device),spi_freq=90000000,rst=RST,dc=DC,bl=BL)
        disp.Init() # Initialize library.
        #disp.clear() # Clear display.
        bg = Image.new("RGB", (disp.width, disp.height), "BLACK")
        draw = ImageDraw.Draw(bg)
        # display with hardware SPI:
        for i in range(180):
            if (doInterrupt==1):
                doInterrupt = 0
                break
            else:
                image = Image.open(directory+'/emotion/'+emotion+'/frame'+str(i)+'.png')	
                image = image.rotate(180)
                disp.ShowImage(image)
        showOn = 0
        disp.module_exit()
        logging.info("quit:")
    except IOError as e:
        logging.info(e)    
    except KeyboardInterrupt:
        disp.module_exit()
        logging.info("quit:")
        exit()

def run_flask():
    from config_server import app
    app.run(debug=True)

def run_sensors(config_data):
    subprocess.Popen([sys.executable, script_path, json.dumps(config_data)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    global doInterrupt, showOn

    # Start the Flask server detached
    logging.info("Starting Flask server")
    cfg_server_process = subprocess.Popen(
    ["waitress-serve", "--host=0.0.0.0", "--port=5000", "config_server:app"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
    )   
    logging.info("Flask server started")

    # Wait until the Flask server has a valid configuration
    url = 'http://127.0.0.1:5000/get_config'
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                config_data = response.json()
                # Check if all required configs are available
                if all(value != "" for value in config_data.values()):
                    break
            logging.info("Waiting for valid configuration...")
        except requests.exceptions.ConnectionError:
            logging.info("Waiting for Flask server to start...")
        time.sleep(1)

    logging.info("Valid configuration received")

    # start sensors script detached
    logging.info("Starting sensors script")
    sensor_server_process = subprocess.Popen([sys.executable, script_path, config_data], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # sensors script will send data to this server
    previousData = 'happy'
    show('happy')
    conn, addr = server.accept()
    conn.settimeout(0.1)
    while True:
        try:
            data = conn.recv(5).decode()
            #print(data)
            if (previousData != data):
                print(data)
                doInterrupt = 1
                previousData = data
                show(data)
        except socket.timeout:
            if showOn!=1:
                show(previousData)

                
if __name__=='__main__':
    main()
    cfg_server_process.terminate()
    sensor_server_process.terminate()
