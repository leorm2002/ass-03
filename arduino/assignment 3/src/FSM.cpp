#include "FSM.h"
#include <Arduino.h>

void FSM::init( SerialIO& serial) {
    currentState = AUTOMATIC;
    this->serial = serial;
}

void FSM::update(volatile bool* buttonPressed, volatile bool* serialDataReceived, int serialValue, Potentiometer& pot, ServoController& servo, Display& display) {
    bool updated = false;

    if (*buttonPressed) {
        *buttonPressed = false;
        serial.debug("Button pressed switching state, new state:" + String(currentState == AUTOMATIC ? "Manual" : "Automatic"));
        switchState();
    }

    int angle = 0;

    if (currentState == AUTOMATIC) {
        if (*serialDataReceived) {
            *serialDataReceived = false;
            if(serialValue < 0 || serialValue > 100) {
                return;
            }
            angle = map(serialValue, 0, 100, 0, 180);
            serial.debug("Recieved a new level " + String(serialValue) + " mapping to angle: " + String(angle));
        }else {
            angle = servo.getAngle();
        }
    } else {
        int potValue = pot.read();
        angle = map(potValue, 0, 1023, -1, 181); // mappo a -1 e 181 e poi applico min e max perchè il potenziometro ha problemi con i fondoscala
        angle = constrain(angle, 0, 180);
        delay(10);//debounce lettura analogica
    }

    updated = servo.getAngle() != angle;
    display.update(currentState, angle);

    if(updated == true) {        
        serial.debug("Updating servo angle");
        servo.setAngle(angle);
    }
}

void FSM::switchState() {
    if (currentState == AUTOMATIC) {
        currentState = MANUAL;
    } else {
        currentState = AUTOMATIC;
    }
}
