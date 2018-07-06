import paho.mqtt.client as mqtt
from datetime import timedelta

#Connection parameters
SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "81b6f448add842a29d5a476d4fa112a8"
USERNAME  = "json+device"
CLIENT_ID = "urn:lo:nsid:samples:device1"

#Publications parameters
TOPIC="dev/data"
qos = 1


def on_connect(client, userdata, flags, rc):
    print("Connected in device mode with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(sampleClient, userdata, msg):
    print(msg.topic+" "+str(msg.payload))



sampleClient = mqtt.Client(CLIENT_ID, clean_session=True, userdata = None, protocol=mqtt.MQTTv311, transport="tcp")
sampleClient.on_connect = on_connect
sampleClient.on_message = on_message
sampleClient.username_pw_set(USERNAME,password = list(API_KEY)) # use device mode and set the password
# now connect to LO
sampleClient.connect(SERVER, PORT, 60)

# create message


sampleClient.loop_forever()
