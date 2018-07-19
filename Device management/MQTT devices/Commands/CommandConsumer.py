#  **
#  * This sample will demonstrate how to receive a command  in a  device : device1
#  * Just create the command in Live Objects UI  and run the sample
#  **

import paho.mqtt.client as mqtt
from datetime import datetime

class CommandConsumer():
    """docstring for CommandConsumer."""

    #Connection parameters
    SERVER = "https://liveobjects.orange-business.com/api/v0/"
    PORT = 1883
    API_KEY = "YOUR API_KEY"
    USERNAME = "json+device"
    CLIENT_ID = "urn:lo:nsid:samples:device1"

    ##Publications parameters
    TOPIC = "dev/cmd"
    qos = 1
    KEEP_ALIVE_INTERVAL = 30
    def __init__(self):
        pass

    def on_connect(client, userdata, flags, rc):
        print("Connected in device mode with result code "+str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(TOPIC)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(sampleClient, userdata, msg):
        print(msg.topic+" "+str(msg.payload))


    def main(arg):
        sampleClient = mqtt.Client(CLIENT_ID, clean_session=True, userdata = None, protocol=mqtt.MQTTv311, transport="tcp")
        sampleClient.on_connect = on_connect
        sampleClient.on_message = on_message
        sampleClient.username_pw_set(USERNAME,password = list(API_KEY)) # use device mode and set the password
        # now connect to LO
        sampleClient.connect(SERVER, PORT, 60)
