#ifndef DISPLAY_H
#define DISPLAY_H

#include <LiquidCrystal_I2C.h>
#include "SerialIO.h"
#include "State.h"

class Display {
public:
    Display(int addr, int cols, int rows);
    void init(SerialIO& serial);
    void update(State mode, int angle);
    void printMsg(String msg);
    
private:
    bool needUpdate(String mode, int angle);
    String modeToStr(State mode);
    LiquidCrystal_I2C lcd;
    SerialIO serial;
    int cols;
    int rows;
    String mode; 
    int angle;
};

#endif
