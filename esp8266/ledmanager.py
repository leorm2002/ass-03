from led import Led
from constants import RED_LED, GREEN_LED

class LedManager:
    def __init__(self):
        self.red = Led(RED_LED, "red")
        self.green = Led(GREEN_LED, "green")

    def green_mode(self):
        self.red.turn_off()
        self.green.turn_on()

    def red_mode(self):
        self.red.turn_on()
        self.green.turn_off()        
        
