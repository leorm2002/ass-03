
import time
import paho.mqtt.client as paho
import uvicorn
from fastapi import FastAPI
from wrap import *
app = FastAPI()
broker="broker.hivemq.com"
topic = "mqtt/naddeil/iot/3"
client = None
msgs = []
controller = None


#callback actions
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print("message received ", msg)
    # try to parse the message to a json dict
    # if it fails, just append the message as a string

#endoints

@app.get("/publish/{msg}")
async def publish(msg: str):
    global client
    client.publish(topic, msg)

@app.get("/stop")
async def stop():
    global client
    client.disconnect() #disconnect
    client.loop_stop() #stop loop

def format_level(level):
    return f"{{\"level\": {level}}}"

@app.get("/sendLevel/{level}")
async def send_level(level: int):
    global client
    level = format_level(level)
    print("sending ",level)
    client.publish(topic,level)

@app.on_event("startup")

@app.get("/getmessages")
async def get_messages():
    return msgs


if __name__ == '__main__':
    #debug mode
    uvicorn.run("main:app", host='0.0.0.0', port=8001, reload=True)
    print("running")