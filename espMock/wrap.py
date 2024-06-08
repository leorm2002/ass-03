client = None
import paho.mqtt.client as paho

broker="broker.hivemq.com"
topic = "mqtt/naddeil/iot/3"
client = None
msgs = []
controller = None


def format_level(level):
    return f"{{\"level\": {level}}}"

async def send_level(level: int):
    global client
    level = format_level(level)
    #print("sending ",level)
    #client.publish(topic,level)

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received ", msg)
    # try to parse the message to a json dict
    # if it fails, just append the message as a string

def startup_event():
    global client
    client= paho.Client(paho.CallbackAPIVersion.VERSION1)
    ######Bind function to callback
    client.on_message=on_message
    print("connecting to broker ",broker)
    client.connect(broker)#connect
    client.loop_start() #start loop to process received messages
    client.subscribe(topic)#subscribe
    print("Connected ")
