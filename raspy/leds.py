import os 
import neopixel
import board

class ledcontroller:
    def __init__(self,boardpin=board.D18,n_leds=80):
        self.pixels = neopixel.NeoPixel(boardpin,n_leds)
        self.colors = [(0,0,0)]*5

    def setPixelRow(color,row):
        if row > 17:
            return
        elif row > 14:
            self.pixels[9+14+1+row] = color
            self.pixels[9+14+2*17-row] = color
        elif row > 9:
            self.pixels[9+14+1+row] = color
            self.pixels[9+14+2*17-row] = color
        elif row > 0:

        else:
            return
        # 9 14 17



