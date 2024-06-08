import paho.mqtt.client as paho
from const import MQTT_BROKER, MQTT_TOPIC

class MqttClient:
    def __init__(self, func) -> None:
        self.client= paho.Client(paho.CallbackAPIVersion.VERSION1)
        ######Bind function to callback
        self.client.on_message=func
        print("connecting to broker ",MQTT_BROKER)
        self.client.connect(MQTT_BROKER)#connect
        self.client.loop_start() #start loop to process received messages
        self.client.subscribe(MQTT_TOPIC)#subscribe
        print("Connected ")
    def send_message(self,msg):
        self.client.publish(MQTT_TOPIC, msg)
    def shutdown(self):
        global client
        client.disconnect() #disconnect
        client.loop_stop() #stop loop
