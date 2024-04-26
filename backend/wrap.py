import paho.mqtt.client as paho
from const import MQTT_BROKER, MQTT_TOPIC

broker= MQTT_BROKER
topic = MQTT_TOPIC
client = None

def send_message(msg):
    global client
    client.publish(topic, msg)

def startup(func):
    global client
    client= paho.Client(paho.CallbackAPIVersion.VERSION1)
    ######Bind function to callback
    client.on_message=func
    print("connecting to broker ",broker)
    client.connect(broker)#connect
    client.loop_start() #start loop to process received messages
    client.subscribe(topic)#subscribe
    print("Connected ")

def shutdown():
    global client
    client.disconnect() #disconnect
    client.loop_stop() #stop loop