#ifndef POTENTIOMETER_H
#define POTENTIOMETER_H

class Potentiometer {
public:
    Potentiometer(int pin);
    void init();
    int read();
    
private:
    int pin;
};

#endif
