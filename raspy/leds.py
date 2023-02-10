import os 
import neopixel
import board

class ledcontroller:
    def __init__(self,boardpin=board.D18,n_leds=80):
        self.pixels = neopixel.NeoPixel(boardpin,n_leds)
        self.colors = [(0,0,0)]*5

    #LED Row Distribution
    # 7 14 17 17 14 9        
       
    def setPixelRow(self,color,row):
        if row > 16:
            return
        elif row > 13:
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
        elif row > 8:
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            self.pixels[7-1+14-row] = color
            self.pixels[7-1+14+(2*17)+row] = color
            pass
        elif row > 6
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            pass
        elif row >= 0:
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            pass
        else:
            return
        




