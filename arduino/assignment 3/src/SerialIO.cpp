#include "SerialIO.h"

SerialIO::SerialIO(){}


void SerialIO::init() {
    debugEnabled = false;
}

void SerialIO::debug(String msg){
    if(this-> debugEnabled){
        Serial.print("Debug: ");
        Serial.println(msg);
    }
}

void SerialIO::setDebugEnabled(boolean debugEnabled){
    this->debugEnabled = debugEnabled;
}
