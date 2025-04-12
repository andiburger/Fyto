import time
import logging
from paho.mqtt import client as mqtt_client

_LOGGER = logging.getLogger(__name__)

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

def connect_mqtt(broker, port, client_id, username=None, password=None):
    """
    Connect to the MQTT broker.
    Args:
        broker (str): The MQTT broker address.
        port (int): The port to connect to.
        client_id (str): The client ID for the connection.
        username (str, optional): The username for authentication. Defaults to None.
        password (str, optional): The password for authentication. Defaults to None.
    Returns:
        mqtt.Client: The MQTT client instance.
    """
    def on_connect(client, userdata, flags, rc):
        """
        Callback function for when the client connects to the broker.
        Args:
            client (mqtt.Client): The MQTT client instance.
            userdata: User-defined data of any type.
            flags: Response flags sent by the broker.
            rc (int): The connection result code.
        """
        if rc == 0:
            _LOGGER.info("Connected to MQTT Broker!")
        else:
            _LOGGER.error("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    if username:
        client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_disconnect(client, userdata, rc):
    """
    Callback function for when the client disconnects from the broker.
    Args:
        client (mqtt.Client): The MQTT client instance.
        userdata: User-defined data of any type.
        rc (int): The disconnection result code.
    """
    _LOGGER.info("Disconnected with result code: %s", rc)
    reconnect_count, reconnect_delay = 0, FIRST_RECONNECT_DELAY
    while reconnect_count < MAX_RECONNECT_COUNT:
        _LOGGER.info("Reconnecting in %d seconds...", reconnect_delay)
        time.sleep(reconnect_delay)
        try:
            client.reconnect()
            _LOGGER.info("Reconnected successfully!")
            return
        except Exception as err:
            _LOGGER.error("%s. Reconnect failed. Retrying...", err)
        reconnect_delay *= RECONNECT_RATE
        reconnect_delay = min(reconnect_delay, MAX_RECONNECT_DELAY)
        reconnect_count += 1
    _LOGGER.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)