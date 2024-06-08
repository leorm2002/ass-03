#include "Display.h"

Display::Display(int addr, int cols, int rows) : lcd(addr, cols, rows) {
    this->cols = cols;
    this->rows = rows;
}
void Display::init(SerialIO& serial) {
    lcd.init();
    lcd.backlight();
    this->serial = serial;
}

void Display::printMsg(String msg) {
    lcd.clear();
    int len = constrain(msg.length(), 0, cols* rows);

    for(int i = 0; i < len; i++) {
        int x = len < 16 ? 0 : 1;
        int y = len < 16 ? i : i - 16;
        lcd.setCursor(y, x);
        lcd.print(msg[i]);
    }
}

bool Display::needUpdate(String mode, int angle){
    if (mode != this->mode || angle != this->angle){
        return true;
    }
    return false;
}
String Display::modeToStr(State mode){
    return mode == AUTOMATIC ? "Automatic" : "Manual";
}

void Display::update(State mode, int angle) {
    String modeStr = modeToStr(mode);
    if(!needUpdate(modeStr, angle)){
        return;
    }
    this->mode = modeStr;
    this->angle = angle;
    lcd.clear();
    String firstLine = "Mode: " + modeStr;
    for(int i = 0; i < firstLine.length(); i++) {
        lcd.setCursor(i, 0);
        lcd.print(firstLine[i]);
    }
    String secondLine = "Angle: " + String(angle);
    for(int i = 0; i < secondLine.length(); i++) {
        lcd.setCursor(i, 1);
        lcd.print(secondLine[i]);
    }
}
