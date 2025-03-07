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


# path to sensors script
script_path = 'sensors.py'

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

def main():
    global doInterrupt, showOn
    url = 'http://127.0.0.1:5000/get_config'
    response = requests.get(url)
    if response.status_code == 200:
        config_data = response.json() 
    else:
        logging.error(f"Error: {response.status_code}")
    # TODO check if all configs are available
    # if not inform user and exit
    # start sensors script detached
    logging.info("Starting sensors script")
    subprocess.Popen([sys.executable, script_path, config_data], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
    try:
        # get configuration from server
        url = 'http://127.0.0.1:5000/get_config'
        response = requests.get(url)
        if response.status_code == 200:
            config_data = response.json() 
            print(config_data)
        else:
            print(f"Error: {response.status_code}")
        main()
    except KeyboardInterrupt:
        exit()
