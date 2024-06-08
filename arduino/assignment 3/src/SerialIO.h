#include <Arduino.h>

#ifndef SERIALIO_H
#define SERIALIO_H

class SerialIO {
public:
    SerialIO();
    void init();
    void debug(String msg);
    void setDebugEnabled(bool debugEnabled);
private:
    bool debugEnabled;
};

#endif
