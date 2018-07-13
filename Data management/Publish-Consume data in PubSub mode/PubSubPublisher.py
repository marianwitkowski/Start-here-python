# @Author: Moustapha KEBE <kebson>
# @Date:   2018-07-12T14:58:01+02:00
# @Email:  mktapha@gmail.com
# @Last modified by:   kebson
# @Last modified time: 2018-07-13T14:18:10+02:00



import paho.mqtt.client as mqtt
from datetime import datetime


SERVER = "liveobjects.orange-business.com"
PORT = 1883
API_KEY   = "Your API_KEY"
USERNAME  = "payload+bridge"
CLIENT_ID = "myFifoClientId"

#Publications parameters
TOPIC="pubsub/pubSubSampleTopic" # topic to publish to
qos = 1

def on_connect(client, userdata, flags, rc):
    print("Connected in bridge mode with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe(TOPIC)

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

# send your message to the topic
msg = "Message published on pubsub topic on "+datetime.now().isoformat()

sampleClient.loop_start()
sampleClient.publish(TOPIC, msg, qos)
print ("Message published")

# Disconnect
sampleClient.disconnect()
print("Disconnected")
