import paho.mqtt.client as mqtt
from jsonRouter.LoSampleRouter import *
from datetime import datetime
import numpy as np
import json
import time

# /**
#  * Application connects to LO and publish messages to the router.
#  *
#  * Messages can be consume from a "routerConsumer", but your consumer application has to be running before you send messages from the publisher
#  * You can also consume message in fifo mode (use the MqttFifoSample (FifoConsumer.py) after having declared a binding in Live Objects.
#  * In that case your message can be consumed
#  *
#  */

#Connection parameters
SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "You API_KEY"
USERNAME  = "payload+bridge"
CLIENT_ID = "myClientID"

#Publications parameters
TOPIC="router/~event/v1/data/new"
qos = 1
var = [1,5,4] # just a test array

def on_connect(client, userdata, flags, rc):
    print("Connected in payload+bridge mode with result code "+str(rc))

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
LoData = LoRouterData()

msgDt = datetime.now().isoformat()
LoRouterData.streamId = "sampleStream2"
LoRouterData.model = "sampleModel2"
LoRouterData.timestamp = msgDt
LoRouterData.tags = np.array(["myTag1","Model.Prototype"])
LoRouterData.value = myData
myData.payload = "Message from bridgeModeSample (payload+bridge) to router data on " + msgDt;
data = '{"s": "'+LoRouterData.streamId+'","ts":"'+LoRouterData.timestamp+'", "m":"'+LoRouterData.model+'", "v": {"payload": "'+myData.payload+'"},"t":'+str(LoRouterData.tags)+'  }'
print data

for o in (var):
# Send your message
    sampleClient.publish(TOPIC, data, qos)
    print ("Message published")

# Disconnect
sampleClient.disconnect()
print("Disconnected")
