from const import *
from level_history import LevelHistory
from pydantic import BaseModel
from serialManager import SerialManager
from state_utils import State, getState
from wrap import send_message


class State(BaseModel):
    state: str
    levels: list[float]
    valve_status: float

class Controller:

    def __init__(self, serialManager: SerialManager):
        self.set_frequency(DEFAULT_FREQ)
        self.levelHistory = LevelHistory()
        self.serialManager = serialManager
        print("Controller started")
        print(".....")

    def processWaterLevel(self, level):
        print("Processing water level: ", level)
        print(".....")
        self.levelHistory.addLevel(level)
        state = getState(level)
        self.set_frequency(state.frequency)
        self.set_valve_status(state.valve_status)
        self.state = state.state

    def format_freq(self, freq):
        return f"{{\"{FRERQUENCY}\": {freq}}}"

    def set_frequency(self, freq):
        self.freq = freq
        print("Setting frequency: ", freq)
        print(".....")
        send_message(self.format_freq(freq))

    def set_valve_status(self, status):
        print("Setting valve status: ", status)
        print(".....")
        self.valve_status = status
        self.serialManager.set_opening(status)

    def getState(self):
        return State(state=self.state, levels=self.levelHistory.getLevels(), valve_status=self.valve_status)