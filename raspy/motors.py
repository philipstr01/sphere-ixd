import RPi.GPIO as GPIO
from time import sleep

"""
# anpassen, falls andere Sequenz
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

class motor:
    def __init__(self,coil_A_1_pin,coil_A_2_pin,coil_B_1_pin,coil_B_2_pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.coil_A_1_pin = coil_A_1_pin
        self.coil_A_2_pin = coil_A_2_pin
        self.coil_B_1_pin = coil_B_1_pin
        self.coil_B_2_pin = coil_B_2_pin
        #GPIO.setup(enable_pin, GPIO.OUT)
        GPIO.setup(coil_A_1_pin, GPIO.OUT)
        GPIO.setup(coil_A_2_pin, GPIO.OUT)
        GPIO.setup(coil_B_1_pin, GPIO.OUT)
        GPIO.setup(coil_B_2_pin, GPIO.OUT)

    #GPIO.output(enable_pin, 1)
    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.coil_A_1_pin, w1)
        GPIO.output(self.coil_A_2_pin, w2)
        GPIO.output(self.coil_B_1_pin, w3)
        GPIO.output(self.coil_B_2_pin, w4)

    def forward(self, delay, steps):
        for i in range(steps):
            for j in range(StepCount):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay)

    def backwards(self, delay, steps):
        for i in range(steps):
            for j in reversed(range(StepCount)):
                self.setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
                time.sleep(delay)
"""
time = 0.001
class motor:
    def __init__(self,A,B,C,D):
        GPIO.setmode(GPIO.BOARD)
        # PIN-Assignment
        self.A=A
        self.B=B
        self.C=C
        self.D=D
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
        sleep (time)
        GPIO.output(self.D, False)
    def Step2(self):
        GPIO.output(self.D, True)
        GPIO.output(self.C, True)
        sleep (time)
        GPIO.output(self.D, False)
        GPIO.output(self.C, False)
    def Step3(self):
        GPIO.output(self.C, True)
        sleep (time)
        GPIO.output(self.C, False)
    def Step4(self):
        GPIO.output(self.B, True)
        GPIO.output(self.C, True)
        sleep (time)
        GPIO.output(self.B, False)
        GPIO.output(self.C, False)
    def Step5(self):
        GPIO.output(self.B, True)
        sleep (time)
        GPIO.output(self.B, False)
    def Step6(self):
        GPIO.output(self.A, True)
        GPIO.output(self.B, True)
        sleep (time)
        GPIO.output(self.A, False)
        GPIO.output(self.B, False)
    def Step7(self):
        GPIO.output(self.A, True)
        sleep (time)
        GPIO.output(self.A, False)
    def Step8(self):
        GPIO.output(self.D, True)
        GPIO.output(self.A, True)
        sleep (time)
        GPIO.output(self.D, False)
        GPIO.output(self.A, False)
    def forward(self,j):
        for i in range (512):
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()
        GPIO.cleanup()
