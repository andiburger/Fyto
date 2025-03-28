from paho.mqtt import client as mqtt_client
import logging
import time

_LOGGER = logging.getLogger(__name__)
FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60


class MQTTClient:
    def __init__(self, broker, port, topic, username=None, password=None, client_id=None):
        """
        Initializes the MQTT client with the provided parameters.
        :param broker: MQTT broker address
        :param port: MQTT broker port
        :param topic: MQTT topic to subscribe to
        :param username: MQTT username (optional)
        :param password: MQTT password (optional)
        :param client_id: MQTT client ID (optional)
        """
        self.broker = broker
        self.port = port
        self.topic = topic
        self.username = username
        self.password = password
        self.client = None 
        self.client_id = client_id

    # Connect to MQTT
    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                _LOGGER.info("Connected to MQTT Broker!")
            else:
                _LOGGER.error("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        self.client = mqtt_client.Client(self.client_id)

        if self.username:
            self.client.username_pw_set(self.username, self.password)
        self.client.on_connect = on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(self.broker, self.port)

    # Disconnect Callback
    def on_disconnect(self, client, userdata, rc):
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

    def loop_start(self):
        """
        Starts the MQTT loop to process network traffic and callbacks.
        """
        self.client.loop_start()

    def loop_stop(self):
        """
        Stops the MQTT loop.
        """
        self.client.loop_stop()
        self.client.disconnect()
        _LOGGER.info("Disconnected from MQTT Broker!")
        self.client = None
        _LOGGER.info("MQTT client set to None")
        self.client_id = None
        _LOGGER.info("MQTT client_id set to None")
        self.topic = None
        _LOGGER.info("MQTT topic set to None")
        self.broker = None
        _LOGGER.info("MQTT broker set to None")
        self.port = None
        _LOGGER.info("MQTT port set to None")
        self.username = None
        _LOGGER.info("MQTT username set to None")
        self.password = None
    
    def publish(self, topic, msg):
        """
        Publishes a message to the specified topic.
        :param topic: MQTT topic to publish to
        :param msg: Message to publish
        """
        if self.client is None:
            raise ValueError("MQTT client is not connected. Call connect_mqtt() first.")
        if not topic:
            raise ValueError("Topic cannot be None or empty.")
        if not msg:
            raise ValueError("Message cannot be None or empty.")
        if not isinstance(msg, str):
            raise ValueError("Message must be a string.")
        if not isinstance(topic, str):
            raise ValueError("Topic must be a string.")
        self.client.publish(topic=topic, payload=msg)
        _LOGGER.info(f"Published message '{msg}' to topic '{topic}'")
    
    def subscribe(self, topic):
        """
        Subscribes to a specified topic.
        :param topic: MQTT topic to subscribe to
        """
        if self.client is None:
            raise ValueError("MQTT client is not connected. Call connect_mqtt() first.")
        if not topic:
            raise ValueError("Topic cannot be None or empty.")
        if not isinstance(topic, str):
            raise ValueError("Topic must be a string.")
        def on_message(client, userdata, msg):
            _LOGGER.info(f"Received message '{msg.payload.decode()}' from topic '{msg.topic}'")
        self.client.subscribe(topic)
        self.client.on_message = on_message
        _LOGGER.info(f"Subscribed to topic '{topic}'")
    
