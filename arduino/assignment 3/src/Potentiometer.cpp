#include "Potentiometer.h"
#include <Arduino.h>

Potentiometer::Potentiometer(int pin) : pin(pin) {}

void Potentiometer::init() {
    pinMode(pin, INPUT);
}

int Potentiometer::read() {
    return analogRead(pin);
}
