from machine import Pin

class Led:
    def __init__(self, pin_number, color = None):
        self.pin_number = pin_number
        self.color = color
        self.pin = Pin(pin_number, mode=Pin.OUT, pull=None)
        self.pin.value(0)

    def turn_on(self):
        self.pin.value(1)
        print("Led ", self.pin_number, self.color, " on")
    
    def turn_off(self):
        self.pin.value(0)
        print("Led ", self.pin_number, self.color, " off")
        
