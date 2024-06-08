#include "ServoController.h"
#include "Potentiometer.h"
#include "Display.h"
#include "SerialIO.h"
#include "FSM.h"
#include <Arduino.h>

#define BUTTON_PIN 2
#define POT_PIN A1
#define SERVO_PIN 9
#define LCD_ADDR 0x27
#define LCD_COLS 16
#define LCD_ROWS 2

SerialIO serial;
ServoController servo(SERVO_PIN);
Potentiometer pot(POT_PIN);
Display display(LCD_ADDR, LCD_COLS, LCD_ROWS);
FSM fsm;

volatile bool buttonPressed = false;
volatile bool serialDataReceived = false;
volatile int serialValue = 0;
void buttonISR() {
    buttonPressed = true;
    delay(30); // debounce
}

void serialEvent() {
    Serial.println("Serial data received");
    serialValue = Serial.parseInt();
    serialDataReceived = true;
}

void setup() {

    Serial.begin(9600);
    Serial.println("Starting setup");
    serial.init();
    serial.setDebugEnabled(true);
    serial.debug("Serial debugging enabled");
    servo.init(serial);
    display.init(serial);
    fsm.init(serial);
    display.printMsg("Avviato...");

    serial.debug("Setup complete");
    pinMode(BUTTON_PIN, INPUT);
    attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), buttonISR, RISING);
}

void loop() {
    fsm.update(&buttonPressed , &serialDataReceived, serialValue, pot, servo, display);

        
    if(buttonPressed != false) {
        Serial.println("Button pressed");
    }
}
