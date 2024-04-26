from pydantic import BaseModel
from const import WL1, WL2, WL3, WL4, F1, F2, A0, A1, A2, A3


class State(BaseModel):
    state: str
    frequency: float
    valve_status: float

def getState(level):
        #se acqua < WL1 => ALARM-TOO-LOW, frequenza F1, apertura 0%
        if level < WL1:
            return logAndReturn(State(state="ALARM-TOO-LOW", frequency=F1, valve_status=A0))
        #se acqua in range [WL1, WL2] allora => NORMAL, frequenza F1, apertura 25%
        elif WL1 <= level <= WL2:
            return logAndReturn(State(state="NORMAL", frequency=F1, valve_status=A1))
        #se acqua ]WL2, WL3] => PRE-ALARM-TOO-HIGH, F2, apertura 25%
        elif WL2 < level <= WL3:
            return logAndReturn(State(state="PRE-ALARM-TOO-HIGH", frequency=F2, valve_status=A1))
        #se acqua ]WL2, WL3] => ALARM-TOO-HIGH, F2, apertura 50%
        elif WL3 < level <= WL4:
            return logAndReturn(State(state="ALARM-TOO-HIGH", frequency=F2, valve_status=A2))
        #se acqua > WL4 => ALARM-TOO-HIGH-CRITIC, apertura 100% 
        elif level > WL4:
            return logAndReturn(State(state="ALARM-TOO-HIGH-CRITIC", frequency=F2, valve_status=A3))
        else:
            print("Error: water level not in range")
            print(".....")
def logAndReturn(state: State):
    print("State: ", state.state)
    print("Frequency: ", state.frequency)
    print("Valve status: ", state.valve_status)
    print()
    return state