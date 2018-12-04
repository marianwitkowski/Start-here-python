**Mqtt "pubsub sample"**

#Objectives
These sample will demonstrate how to communicate from your device in Java in "pubsub mode" (Bridge mode, publishing to pubsub or consuming from).


#Samples
You will find in this project 2 main classes illustrating :

- Publish data in Live Object : **PubSubPublisher**
- Consume date from Live Objects : **PubSubConsumer**

#Building the samples
The project is a maven project. You are free to use any IDE of your choice to build the project.


#Using the samples

1. Set The API_KEY and run the sample


#Publishing data
Use the PubSubPublisher class. 

#Consuming data
Use the PubSubConsumer class. It you start it after running the PubSubPublisher class, you will notice that the messages are not delivered when running it (messages are lost).
Start the PubSubPublisher : your messages are delivered.
