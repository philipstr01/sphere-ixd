import os 
import neopixel
import board
import time

def t_add(t1,t2):
    return tuple(map(sum, zip(t1, t2)))

def t_mul(s,t):
    return tuple([s*x for x in t])


class ledcontroller:
    def __init__(self,boardpin=board.D18,n_leds=80):
        self.pixels = neopixel.NeoPixel(boardpin,n_leds)
        self.colors = self.colors = [(174,126,235),(152,227,245),(120,222,104),(245,210,59),(224,114,88)]

    #LED Row Distribution
    # 7 14 17 17 14 9        
       
    def setPixelRow(self,color,row):
        if row > 16:
            return
        elif row > 13:
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
        elif row > 8:
            self.pixels[7-1+14-row] = color
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            self.pixels[7+14+(2*17)+row] = color
            pass
        elif row > 6:
            self.pixels[7-1+14-row] = color
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            self.pixels[7+14+(2*17)+row] = color
            self.pixels[78-1-row] = color
            
            pass
        elif row >= 0:
            self.pixels[row] = color
            self.pixels[7-1+14-row] = color
            self.pixels[7+14+row] = color
            self.pixels[7-1+14+(2*17)-row] = color
            self.pixels[7+14+(2*17)+row] = color
            self.pixels[78-1-row] = color
            pass
        else:
            return
        
    def colorGradient(self,t):
        if t > 1:
            c = self.colors[4]
        elif t > 3/4:
            c = t_add(t_mul(4*(t-3/4),self.colors[4]),t_mul((1-4*(t-3/4)),self.colors[3]))
        elif t > 2/4:
            c = t_add(t_mul(4*(t-2/4),self.colors[3]),t_mul((1-4*(t-2/4)),self.colors[2]))
        elif t > 1/4:
            c = t_add(t_mul(4*(t-1/4),self.colors[2]),t_mul((1-4*(t-1/4)),self.colors[1]))
        elif t > 0/4:
            c = t_add(t_mul(4*t,self.colors[1]),t_mul((1-4*t),self.colors[0]))
        else:
            c = self.colors[0]

        c = list(c)
        for i in range(len(c)):
            if c[i] > 255:
                c[i] = 255
            elif c[i] < 0:
                c[i] = 0

        c = tuple(c)
        return c

    def colorRows(self,t):
        n = 0
        b = 1/64
        while n<17:
            print(self.colorGradient(t))
            self.setPixelRow(self.colorGradient(t+b*n),n)
            n += 1

    def colorCycle(self,a,b):
        x = a
        while x <= b:
            self.colorRows(x)
            x+=1/8
            time.sleep(2)

        
        




