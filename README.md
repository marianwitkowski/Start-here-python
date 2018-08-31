This document describes how to use the main features of Live Objects to develop your IoT application.



# Getting Started Guide #

This document describes how to use the main features of Live Objects (LO) to develop your IoT application. 

## Terminology: ##

* client: your application that will make Live Objects API calls
* API-KEY: the token that allows you to connect to your own tenant/space in Live Objects
* CLIENT-ID: identifier of the device or of the application currently trying to connect to Live Objects
* endpoint: the URL to access to a function of the API in REST
* header: a user-defined HTTP header to carry information in a REST call


## Before starting ## 

We focus here on the use of the APIs to push and consume data from the “Live Objects Bus” and to perform “device management” operations. 
If you are familiar with the concepts of Live Objects bus (topics, publish mode...), you can skip this chapter.


## 1.1 LIVE OBJECTS BUS ## 

What is Live Objects BUS ? It’s basically a place where you can push information to and from where you can consume this information.
In the IOT world, anybody will have in mind a sample case:

```ruby
Device  : publish data -> Live Objects -> consume by application(s)
```

But you can also configure your device entering data in the web portal:
```ruby
Enter data in Live Objects UI -> consume by your device
```

Publishing or consuming any kind of information, the first relevant question is:

1. How can I do that ?  With Live Objects you will use different protocols, at this time MQTT(S) or HTTP(S)/Rest APIs are available to talk with Live Objects BUS. Choosing the right protocol depends on the Live Objects functionality you want to use.

2. How can I address the bus ? You only need a little information
    a. The server address
    b. A “message box address”. In our case, these message boxes are in fact message queues (messages are queued in them), and we will use the name of “Topic” as the address of these message queues.
    
3. How am I identified ? You will have to use:
    * your own API-KEY
    * a CLIENT-ID
 
## 1.2 TOPIC concepts ## 

We can make a parallel. If you want to send somebody some information, you will need:
    * his country, his town, his street, his street address, his stage, his door number

A Topic is somehow any of this kind of information.
    * country: all people in the country will be able to receive your message
    * country/town/street: all people of the street of the town will be able to receive your message
    * …
    * country/town/street/.../door: only the people living there will be able to receive your message.


In Live Objects, you have predefined parts of the addresses that are fixed, the other are of your choice.


## 1.3 DEVICE MODE VS BRIDGE MODE ## 

You can publish using 2 modes:

Type mode | what for ?
------------ | -------------
Device mode  | the mode for devices to publish directly to Live Objects.</td>
Bridge mode | used when you are using a gateway between your devices and Live Objects.

When using one mode, you must follow the following rules:
The first part of the topic is the type of the topic: pubsub/, fifo/ or router/ for the bridge mode
and dev/ for the “device mode”.
Pay attention that only some addresses will make your data persisting in the Live Objects “data zone”, all others will be available only for your consumers (Elastic search/Kibana impact)


Publish mode  | Type | Address | Persisted in data zone
------------ | ------------- | ------------ | -------------
Device Mode | dev/ | fixed: data, cfg, ... | yes for dev/data , yes for dev/data/xxx
Bridge mode (pubsub) | pubsub/ | - | no
Bridge mode (fifo) | fifo/ | at your choice | no
Bridge mode (router) | router/ | at your choice | no
Bridge mode (router) | router/ | ~event/v1/data/new/typ/+/dev/+/con/+/evt/+/grp, ~event/v1/data/new/typ/+/dev/+/con/+/evt/+/grp/xxx | yes

### 1 Publish data ###
Device mode ? Bridge mode ? How to choose:

    * Device mode is the best mode for device publishing directly to Live Objects
    * Bridge mode is more used when you are using a gateway that hides Live Objects to your device.

### 2 Consume data ###
Live Objects has a very powerful concept: the fifos !
Fifos allow you to consume data from your application, even when your application is down for any reason (of course, while it is down you will not consume anything … , but as soon as your application is up again, all data published in the mean time will be delivered in the right order to your application.
In pubsub mode or router mode, your application has to be up to consume the data at the time they are published to Live Objects

### 3 The big question: topic, fifo and bindings ###
Well: how do I choose a topic to publish to ?, how does this influence the way data will be consumed ?

## 3.1 Mqtt devices ## 
Data published on topic <b>/dev/data/xxx</b>  (xxx may be what you want) can be consumed on a fifo created with routing key <b>~event.v1.data.new.typ.*.dev.*.con.*.evt.*.grp</b>

But  perhaps you need  to route your data to different consumer to best suit your needs. Let’s take an example:
I want to consume the data of some devices to a development environment while some others are used in production.
In that case you can publish and consume your data the following way:
You create 2 fifos, let’s say for example devFifo and prodFifo.
Configure your production application to consume from prodFifo, while your development application will consume from devFifo.
Configure your devices so that devices in production mode and devices used for development will publish to different topics (let’s say for example /dev/data/myprod and /dev/data/mydev.
Then just create two routing keys in Live Objects for your two fifos:

    * prodFifo : ~event.v1.data.new.typ.*.dev.*.con.*.evt.*.grp.myprod
    * devFifo : ~event.v1.data.new.typ.*.dev.*.con.*.evt.*.grp.mydev

Device kind | Topic to publish | Fifo | &nbsp;
------------ | ------------ | ------------ | ------------
production | /dev/data/myprod | prodFifo | ~event.v1.data.new.typ.*.dev.*.con.*.evt.*.grp.myprod
development | /dev/data/mydev | devFifo | ~event.v1.data.new.typ.*.dev.*.con.*.evt.*.grp.mydev

**Important** **:** New topic format will be available the 2nd of October 2018 for all customers. The deprecated topic will be decommissioned in december 2018. Please use the new topic to receive data messages. Please avoid the use of topic event.v1.data.new.#

## 3.2 Lora devices ##
Data sent by Lora devices are automatically available in Live Objects data zone. You only have to decide of the way to consume them.
Best way to take benefit of the Fifo mode: create fifos in Live Objects UI, with a binding rule:

    * ~event.v1.data.new.urn.lora.# : (deprecated and will be decommissioned in december 2018) all messages of all devices
    * ~event.v1.data.new.{DevEUI}.# : (deprecated and will be decommissioned in december 2018) all messages of the device DevEUI
    * ~event.v1.data.new.typ.*.dev.*.con.lora.evt.*.grp.# : all messages of all devices
    * ~event.v1.data.new.typ.*.dev.{deviceId}.con.lora.evt.*.grp.# : all messages of the device, deviceId is the URN of the device: urn:lo:nsid:lora:{devEUI}


# 4 Samples introduction # 

All samples are independent project that you run according your needs.


## 4.1 SAMPLES (PUBLISHING AND CONSUMING) ## 


### 4.1.1 LIVE OBJECTS PARAMETERS ###

Use static constants for all Live Objects parameters. This will certainly not what you will prefer to do in your real application code, but centralizing them in the samples gives you a complete overview of the different parameters.
A first group of parameters defines the connection to Live Objects

```ruby
// Connection parameters
SERVER = "tcp://liveobjects.orange-business.com:1883"; // declare Live Objects end point
API_KEY = "<<YOUR API KEY>>";                             // <-- REPLACE by YOUR API_KEY!
USERNAME="json+device";                                // The option to publish in device mode
CLIENT_ID="urn:lo:nsid:samples:device1";               // in device mode: urn:lo:nsid:{namespace}:{id}
```

Notice that you have to define the connection mode (device mode or bridged mode) when connecting  
Connecting using SSL : you only have to change the SERVER end point to:

```ruby
SERVER mqtts://liveobjects.orange-business.comm:8883
```

The second group of parameters defines the way your message will be published to Live Objects:


```ruby
//Publication parameters
TOPIC="dev/data";  // topic to publish to
int qos = 1;              // set the qos
```

### 4.1.2 JSON STRUCTURE ###

All JSON structures are defined in separate packages.
All JSON structures defined by Live Objects are named the same way: they start with Lo (LoCfg, LoData…). The other ones are your structure that you can change according your needs.

# 5 USING MQTT(S) SAMPLES #

## 5.1 LIST OF SAMPLES ##

For each project listed below, you will find more information in the readme.md

Mode | Project name
------------ | -------------
Device Mode |  [Publish data in device mode] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Data%20management/Publish%20data%20in%20device%20mode)  <br> [Commands] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Device management/MQTT devices/Commands)    <br>   [Configuration] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Device management/MQTT devices/Configuration)  <br> [Publishing info] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Device management/MQTT devices/Publishing infos) 
Bridge Mode / pubSub | [Publish-Consume data in PubSub mode] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Data management/Publish-Consume data in PubSub mode)
Bridge Mode / router | [Publish-consume data in router mode] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Data management/Publish-consume data in router mode)  |  
Bridge Mode / fifo | [Publish-consume data in FIFO mode] (https://github.com/DatavenueLiveObjects/Start-here-python/tree/master/Data management/Publish-consume data in FIFO mode)
