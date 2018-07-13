# @Author: Moustapha KEBE <kebson>
# @Date:   2018-07-12T15:18:22+02:00
# @Email:  mktapha@gmail.com
# @Last modified by:   kebson
# @Last modified time: 2018-07-13T12:10:24+02:00



import paho.mqtt.client as mqtt
from datetime import datetime


SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "e6e10b0cdc50409bab7748f8c4d0dfd2"
USERNAME  = "payload+bridge"
CLIENT_ID = "myFifoClientId"

#Publications parameters
TOPIC="pubsub/pubSubSampleTopic" # topic to publish to
qos = 1
KEEP_ALIVE_INTERVAL = 30 # Must be <= 50


def on_connect(client, userdata, flags, rc):
    print("Connected in bridge mode with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe(TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(sampleClient, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_subscribe(sampleClient, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

print("Runinng consumer appId=" + CLIENT_ID)
sampleClient = mqtt.Client(CLIENT_ID, clean_session=True, userdata = None, protocol=mqtt.MQTTv311, transport="tcp")
sampleClient.on_connect = on_connect
sampleClient.on_message = on_message
sampleClient.on_subscribe = on_subscribe
sampleClient.username_pw_set(USERNAME,password = list(API_KEY)) # use device mode and set the password
sampleClient.reconnect_delay_set(min_delay=1, max_delay=120)

# now connect to LO
print "Connecting to broker:", SERVER
sampleClient.connect(SERVER, PORT, KEEP_ALIVE_INTERVAL)
print "... connected."

sampleClient.subscribe(TOPIC,qos)
sampleClient.loop_forever()
# sampleClient.connect_async(SERVER,PORT, KEEP_ALIVE_INTERVAL,bind_address="")
# print("rc: "+str(rc))
