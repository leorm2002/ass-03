#ifndef SERVOCONTROLLER_H
#define SERVOCONTROLLER_H

#include <Servo.h>
#include "SerialIO.h"

class ServoController {
public:
    ServoController(int pin);
    void init(SerialIO& serial);
    void setAngle(int angle);
    int getAngle();
    
private:
    Servo servo;
    SerialIO serial;
    int pin;
    int angle;
};

#endif
