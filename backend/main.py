import json

import uvicorn
import wrap as mqttWrap
from const import WATER_LEVEL
from controller import Controller, SystemState
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from serialManager import SerialManager

app = FastAPI()
controller = None
serialManager = None

manual = False

templates = Jinja2Templates(directory="templates")

# quando arriva un messaggio prova a fare il parse del messaggio e se c'è il campo WATER_LEVEL chiama il metodo processWaterLevel
def on_message(client, userdata, message):
    if manual:
        print("Manual mode enabled, ignoring message")
    msg = str(message.payload.decode("utf-8"))
    try:
        msg = json.loads(msg)
        if WATER_LEVEL in msg:
            controller.processWaterLevel(msg[WATER_LEVEL], manual)
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
async def get_water_level_datas() -> SystemState:
    """
    Retrieves the water level data from the controller.

    Returns:
        State: The current state of the water level.
    """
    state = controller.getState()
    if manual:
        state.system_mode = "manual"
    else:
        state.system_mode = "automatic"
    return state

@app.post("/setValveStatus")
async def set_opening_status(level: int):
    """
    Sets the status of the valve.

    Parameters:
    - status (int): The opening value to set for the valve.

    Returns:
    - None
    """
    global manual
    manual = True
    controller.set_valve_opening(level)

@app.post("/setAutomatic")
async def set_automatic():
    """
    Sets the valve to automatic mode.

    Returns:
    - None
    """
    global manual
    manual = False

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # todo generazione grafico non funzionante
    return templates.TemplateResponse("index.html", {"request": request})



if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=5000, reload=False)
    print("running")
