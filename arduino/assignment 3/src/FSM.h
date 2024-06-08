#ifndef FSM_H
#define FSM_H

#include "ServoController.h"
#include "Potentiometer.h"
#include "Display.h"
#include "SerialIO.h"
#include "State.h"

class FSM {
public:
    void init(SerialIO& serial);
    void update(volatile bool* buttonPressed, volatile bool* serialDataReceived, int serialValue, Potentiometer& pot, ServoController& servo, Display& display);
    
private:
    State currentState;
    void switchState();
    SerialIO serial;
};

#endif
