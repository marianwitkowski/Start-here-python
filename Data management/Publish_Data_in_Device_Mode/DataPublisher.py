import paho.mqtt.client as mqtt
from jsonDevData.LoSampleData import LoData, SampleData
from datetime import datetime
import numpy as np
import json
import time

#Connection parameters
SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "52fc306744a3447faab861ed8d4f2b77"
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


# Create and fill your connections options
sampleClient = mqtt.Client(CLIENT_ID, clean_session=True, userdata = None, protocol=mqtt.MQTTv311, transport="tcp")
sampleClient.on_connect = on_connect
sampleClient.on_message = on_message
sampleClient.username_pw_set(USERNAME,password = API_KEY) # use device mode and set the password
# now connect to LO
sampleClient.connect(SERVER, PORT, 60)

# # create message
LoData = LoData()
myData = SampleData()

msgDt = datetime.now().isoformat()
LoData.s = "Stream1"
LoData.m = "samplesModel"
LoData.ts = msgDt
LoData.loc = np.array([48.125,2.185])
myData.payload = "Message from deviceMode on dev/data on " + msgDt
myData.temperature=16
myData.hygrometry=11
LoData.v = myData
data = '{"s": "'+CLIENT_ID+'","m":"'+LoData.m+'", "value": {"temperature": '+str(myData.temperature)+', "humidite": '+str(myData.hygrometry)+'}, "location":{"lat":'+str(LoData.loc[0])+', "lon": '+str(LoData.loc[1])+'}   }'

sampleClient.loop_start()
while True:
    # Send your message
    sampleClient.publish(TOPIC, data, qos)
    print ("Message published")
    print(data)
    time.sleep(4)
    # Disconnect
sampleClient.disconnect()
print("Disconnected")
