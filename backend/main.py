import json

import uvicorn
import wrap as mqttWrap
from const import WATER_LEVEL
from controller import Controller, State
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_mqtt import FastMQTT, MQTTConfig
from serialManager import SerialManager

app = FastAPI()
controller = None
serialManager = None

templates = Jinja2Templates(directory="templates")

# quando arriva un messaggio prova a fare il parse del messaggio e se c'è il campo WATER_LEVEL chiama il metodo processWaterLevel
def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    try:
        msg = json.loads(msg)
        if WATER_LEVEL in msg:
            controller.processWaterLevel(msg[WATER_LEVEL])
    except Exception as e:
        print("Error: ", e)

# all'avvio istanzio le mie classi controller e il mio wrap di mqtt
@app.on_event("startup")
async def startup_event():
    global controller
    global serialManager
    mqttWrap.startup(on_message)
    serialManager = SerialManager()
    controller = Controller(serialManager)


@app.get("/getState")
async def get_water_level_datas() -> State:
    """
    Retrieves the water level data from the controller.

    Returns:
        State: The current state of the water level.
    """
    return controller.getState()

@app.get("/test")
async def test():
    """
    Retrieves the status of the valve.

    Returns:
    - float: The status value of the valve.
    """
    return "dwedfe"
@app.post("/setValveStatus")

async def set_valve_status(status: float):
    """
    Sets the status of the valve.

    Parameters:
    - status (float): The status value to set for the valve.

    Returns:
    - None
    """
    controller.set_valve_status(status)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # todo generazione grafico non funzionante
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=9200, reload=True)
    print("running")
