#include "ServoController.h"

ServoController::ServoController(int pin) {
    this->pin = pin;
}

void ServoController::init(SerialIO& serial) {
    servo.attach(pin);
    this->serial = serial;
}

void ServoController::setAngle(int angle) {
    serial.debug("Setting angle to " + String(angle));
    this->angle = angle;
    servo.write(angle + 10); // offset since the servo vibrate when putted to 0
    delay(20);
}

int ServoController::getAngle() {
    return angle;
}
