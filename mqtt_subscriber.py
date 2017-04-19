# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print "Connected with result code "+str(rc)
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/1234/Dev2975702/attrs/temperature", 0)

    
def activate_trigger():
    print "Temperature limit reached: activating actions\n"
    # DEFINE ACTIVATING ACTIONS

def deactivate_trigger():
    print "Temperature below limit: deactivating actions\n"
    # DEFINE DEACTIVATING ACTIONS
    
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
    
    if int(msg.payload) > 25:
        activate_trigger()
    else:
        deactivate_trigger()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("130.206.112.29",1883)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()