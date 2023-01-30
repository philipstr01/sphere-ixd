import RPi.GPIO as GPIO
import time

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
        GPIO.setmode(GPIO.BCM)
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
