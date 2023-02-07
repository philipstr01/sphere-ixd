import RPi.GPIO as GPIO
import copy
from time import sleep
import time

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
    def __init__(self,dict):
        self.arr = list(dict.keys())
        self.dict = dict
        self.time = self.measureDelay()

    def measureDelay(self):
        start = time.time()

        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, True)
            else:
                GPIO.output(m.D, True)
                GPIO.output(m.A, True)

        end = time.time()

        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, False)
            else:
                GPIO.output(m.D, False)
                GPIO.output(m.A, False)

        t = 1e-3 - (len(self.arr)-1)*(end-start)/(len(self.arr))
        if t < 0:
            return 0
        else:
            return t

    
    #parallel motor driving
    def Step1(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, True)
            else:
                GPIO.output(m.D, True)
                GPIO.output(m.A, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, False)
            else:
                GPIO.output(m.D, False)
                GPIO.output(m.A, False)

    def Step2(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, True)
                GPIO.output(m.C, True)
            else:
                GPIO.output(m.A, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.D, False)
                GPIO.output(m.C, False)
            else:
                GPIO.output(m.A, False)

    def Step3(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.C, True)
            else:
                GPIO.output(m.A, True)
                GPIO.output(m.B, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.C, False)
            else:
                GPIO.output(m.A, False)
                GPIO.output(m.B, False)

    def Step4(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.C, True)
                GPIO.output(m.B, True)
            else:
                GPIO.output(m.B, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.C, False)
                GPIO.output(m.B, False)
            else:
                GPIO.output(m.B, False)

    def Step5(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.B, True)
            else:
                GPIO.output(m.B, True)
                GPIO.output(m.C, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.B, False)
            else:
                GPIO.output(m.B, False)
                GPIO.output(m.C, False)

    def Step6(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, True)
                GPIO.output(m.B, True)
            else:
                GPIO.output(m.C, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, False)
                GPIO.output(m.B, False)
            else:
                GPIO.output(m.C, False)

    def Step7(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, True)
            else:
                GPIO.output(m.C, True)
                GPIO.output(m.D, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, False)
            else:
                GPIO.output(m.C, False)
                GPIO.output(m.D, False)

    def Step8(self):
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, True)
                GPIO.output(m.D, True)
            else:
                GPIO.output(m.D, True)
        sleep (self.time)
        for m in self.arr:
            if self.dict[m]:
                GPIO.output(m.A, False)
                GPIO.output(m.D, False)
            else:
                GPIO.output(m.D, False)

    def move(self,x):
        for i in range(int(x*512)):
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
        self.heights = [0]*len(self.marray.arr)

    def changeHeights(self,deltaheights):
        if len(deltaheights) != len(self.marray.arr):
            print("Passed list has not the same length as motors in list!")
            return

        for i in range(len(deltaheights)):
            self.heights[i] += deltaheights[i]
            if deltaheights[i] >= 0:
                self.marray.dict[self.marray.arr[i]] = True
            else:
                self.marray.dict[self.marray.arr[i]] = False
            deltaheights[i] = abs(deltaheights[i])

        tmparr = copy.deepcopy(self.marray)

        while tmparr.arr:
            l = len(deltaheights)
            idx = []
            minV = min(deltaheights)
            for i in range(l):
                if deltaheights[i] == minV:
                    idx.append(i)

            tmparr.move(minV)

            for i in range(l):
                deltaheights[i] -= minV

            if len(idx) == 0:
                continue
            idx.reverse()
            for i in idx:
                del tmparr.arr[i]
                del deltaheights[i]

    def setHeights(self,newheights):
        l = len(self.heights)
        deltaheights = [0]*l
        for i in range(l):
            deltaheights[i] = newheights[i]-self.heights[i]
        self.changeHeights(deltaheights)
    
    def zeroHeights(self):
        self.setHeights(self,[0]*len(self.heights))
    


    
