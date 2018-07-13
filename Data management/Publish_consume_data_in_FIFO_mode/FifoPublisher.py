#
#  * Application connects to LO and publish messages.
#  *
#  * Data published directly on fifo will not be stroed in the datazone, but consumed by a fifo consumer when this client
#  * will be up.
#  * take care that you shouldn't add a routing key to this fifo !
#  *
import paho.mqtt.client as mqtt
from jsonFIFO.LoSampleFIFO import *
from datetime import datetime
import numpy as np
import json
import time

#Connection parameters
SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "YOUR API_KEY"
USERNAME  = "payload+bridge"
CLIENT_ID = "myFifoClientId"

#Publications parameters
TOPIC="fifo/sampleFifo"
qos = 1
var = [1,5,4] # just a test array


def on_connect(client, userdata, flags, rc):
    print("Connected in bridge mode with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(sampleClient, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


# Create and fill your connections options
sampleClient = mqtt.Client(CLIENT_ID, clean_session=True, userdata = None, protocol=mqtt.MQTTv311, transport="tcp")
sampleClient.on_connect = on_connect
sampleClient.on_message = on_message
sampleClient.username_pw_set(USERNAME,password = list(API_KEY)) # use device mode and set the password
# now connect to LO
sampleClient.connect(SERVER, PORT, 60)

# # create message
myData = SampleData()
LoData = LoFifoData()

msgDt = datetime.now().isoformat()
LoFifoData.streamId = "sampleStream"
LoFifoData.model = "sampleModel"
LoFifoData.timestamp = msgDt
LoFifoData.value = myData
myData.payload = "Message from bridgeModeSample (payload+bridge) to fifo/sampleFifo on " + msgDt;
data = '{"s": "'+LoFifoData.streamId+'","ts":"'+LoFifoData.timestamp+'", "m":"'+LoFifoData.model+'", "v": {"payload": "'+myData.payload+'"}  }'
print data

# sampleClient.loop_forever()
for o in (var):
# Send your message
    sampleClient.publish(TOPIC, data, qos)
    print ("Message published")

# Disconnect
sampleClient.disconnect()
print("Disconnected")
