from const import *
from level_history import LevelHistory
from pydantic import BaseModel
from serialManager import SerialManager
from state_utils import getState
from wrap import send_message


class SystemState(BaseModel):
    state: str
    levels: list[float]
    valve_opening: int
    system_mode: str = "automatic"

class Controller:

    def __init__(self, serialManager: SerialManager):
        self.set_frequency(DEFAULT_FREQ)
        self.levelHistory = LevelHistory()
        self.serialManager = serialManager
        #todo default
        self.state_description = "NORMAL"
        self.opening = 0
        print("Controller started")
        print("")

    def processWaterLevel(self, level : float, manual: bool):
        print()
        print("LIVELLO ACQUA: ", level)
        self.levelHistory.addLevel(level)
        system_state = getState(level)
        if not manual:
            self.set_frequency(system_state.sampling_frequency)
            self.set_valve_opening(system_state.valve_opening)
        self.set_state_description(system_state.state_description)

    def format_freq(self, freq):
        return f"{{\"{FRERQUENCY}\": {freq}}}"

    def set_frequency(self, freq):
        self.freq = freq
        send_message(self.format_freq(freq))

    def set_valve_opening(self, opening: int):
        self.opening = opening
        self.serialManager.set_opening(opening)

    def set_state_description(self, state_description):
        self.state_description = state_description


    def getState(self):
        return SystemState(state=self.state_description, levels=self.levelHistory.getLevels(), valve_opening=self.opening)