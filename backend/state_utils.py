from pydantic import BaseModel, Field
from const import WL1, WL2, WL3, WL4, F1, F2, A0, A1, A2, A3


class SystemState(BaseModel):
    state_description: str
    sampling_frequency: int
    valve_opening: int

def getState(level) -> SystemState:
        #se acqua < WL1 => ALARM-TOO-LOW, frequenza F1, apertura 0%
        if level < WL1:
            return logAndReturn(SystemState(state_description="ALARM-TOO-LOW", sampling_frequency=F1, valve_opening=A0))
        #se acqua in range [WL1, WL2] allora => NORMAL, frequenza F1, apertura 25%
        elif WL1 <= level <= WL2:
            return logAndReturn(SystemState(state_description="NORMAL", sampling_frequency=F1, valve_opening=A1))
        #se acqua ]WL2, WL3] => PRE-ALARM-TOO-HIGH, F2, apertura 25%
        elif WL2 < level <= WL3:
            return logAndReturn(SystemState(state_description="PRE-ALARM-TOO-HIGH", sampling_frequency=F2, valve_opening=A1))
        #se acqua ]WL2, WL3] => ALARM-TOO-HIGH, F2, apertura 50%
        elif WL3 < level <= WL4:
            return logAndReturn(SystemState(state_description="ALARM-TOO-HIGH", sampling_frequency=F2, valve_opening=A2))
        #se acqua > WL4 => ALARM-TOO-HIGH-CRITIC, apertura 100% 
        elif level > WL4:
            return logAndReturn(SystemState(state_description="ALARM-TOO-HIGH-CRITIC", sampling_frequency=F2, valve_opening=A3))
        else:
            print("Error: water level not in range")
            print(".....")
def logAndReturn(state: SystemState):
    print("    => Stato sistema: ", state.state_description)
    print("    => Frequenza: ", state.sampling_frequency)
    print("    => Apertura valvola: ", state.valve_opening, "%")
    print()
    return state