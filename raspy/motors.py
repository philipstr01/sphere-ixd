import RPi.GPIO as GPIO
from time import sleep

time = 0.001

class motor:
    def __init__(self,A,B,C,D):
        # PIN-Assignment
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.time = 1e-3
        # defining the PINs
        GPIO.setup(self.A,GPIO.OUT)
        GPIO.setup(self.B,GPIO.OUT)
        GPIO.setup(self.C,GPIO.OUT)
        GPIO.setup(self.D,GPIO.OUT)
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
        GPIO.output(self.D, False)
    # driving the motor
    def Step1(self):
        GPIO.output(self.D, True)
        sleep (self.time)
        GPIO.output(self.D, False)
    def Step2(self):
        GPIO.output(self.D, True)
        GPIO.output(self.C, True)
        sleep (self.time)
        GPIO.output(self.D, False)
        GPIO.output(self.C, False)
    def Step3(self):
        GPIO.output(self.C, True)
        sleep (self.time)
        GPIO.output(self.C, False)
    def Step4(self):
        GPIO.output(self.B, True)
        GPIO.output(self.C, True)
        sleep (self.time)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
    def Step5(self):
        GPIO.output(self.B, True)
        sleep (self.time)
        GPIO.output(self.B, False)
    def Step6(self):
        GPIO.output(self.A, True)
        GPIO.output(self.B, True)
        sleep (self.time)
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
    def Step7(self):
        GPIO.output(self.A, True)
        sleep (self.time)
        GPIO.output(self.A, False)
    def Step8(self):
        GPIO.output(self.D, True)
        GPIO.output(self.A, True)
        sleep (self.time)
        GPIO.output(self.D, False)
        GPIO.output(self.A, False)
    def forward(self,x):
        for i in range(int(512*x)):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()
    def backward(self,x):
        for i in range(int(512*x)):
            self.Step8()
            self.Step7()
            self.Step6()
            self.Step5()
            self.Step4()
            self.Step3()
            self.Step2()
            self.Step1()
class motorarray:
    def __init__(self,arr):
        self.arr = arr
        self.time = 1e-3

    def Step1(self):
        for m in self.arr:
            GPIO.output(m.D, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.D, False)

    def Step2(self):
        for m in self.arr:
            GPIO.output(m.D, True)
            GPIO.output(m.C, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.D, False)
            GPIO.output(m.C, False)

    def Step3(self):
        for m in self.arr:
            GPIO.output(m.C, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.C, False)

    def Step4(self):
        for m in self.arr:
            GPIO.output(m.B, True)
            GPIO.output(m.C, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.B, False)
            GPIO.output(m.C, False)

    def Step5(self):
        for m in self.arr:
            GPIO.output(m.B, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.B, False)

    def Step6(self):
        for m in self.arr:
            GPIO.output(m.A, True)
            GPIO.output(m.B, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.A, False)
            GPIO.output(m.B, False)

    def Step7(self):
        for m in self.arr:
            GPIO.output(m.A, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.A, False)

    def Step8(self):
        for m in self.arr:
            GPIO.output(m.D, True)
            GPIO.output(m.A, True)
        sleep (self.time)
        for m in self.arr:
            GPIO.output(m.D, False)
            GPIO.output(m.A, False)

    def forward(self,x):
        for i in range(x*512):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()

class motorcontroller:
    def __init__(self,marray):
        self.marray=marray
        self.heights = []

    def setheights(self,heights):
        l = len(heights)
        if l != len(self.marray.arr):
            print("Passed list has not the same length as motors in list!")
            return

        self.heights = heights

        tmparr = self.marray #Maybee needs .copy()
        while tmparr.arr:
            idx = []
            minV = min(heights)
            for i in range(l):
                if heights[i] == minV:
                    idx.append(i)

            tmparr.forward(minV)
            for i in idx.reverse():
                del tmparr.arr[i]
                del heights[i]
            
