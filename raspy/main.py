import base_functions
import motors
import RPi.GPIO as GPIO
import time
import neopixel
import board
import leds

#base_functions.download_write_responses()

#df = base_functions.getsurveyDataframe()
#mysurvey = base_functions.getSurveyObject()

#Motor Test script,
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1 = motors.motor(2,3,4,14)
motor2 = motors.motor(15,17,19,27)
motor3 = motors.motor(22,23,24,10)
motor4 = motors.motor(9,11,8,7)
motor5 = motors.motor(5,6,12,13)
marray = motors.motorarray([motor1,motor2,motor3,motor4,motor5])   
contr = motors.motorcontroller(marray)

#main function
def main():
    minheight = 1
    maxheight = 9 + minheight

    chaosHeights = [0.4,0.1,1,0.5,0.2]
    harmonHeights = [0.25,1,0,1,0.25]

    led = leds.ledcontroller()
    led.pixels.fill((0,0,0))
    stress = 0

    motor1 = motors.motor(2,3,4,14)
    motor2 = motors.motor(15,17,19,27)
    motor3 = motors.motor(22,23,24,10)
    motor4 = motors.motor(9,11,8,7)
    motor5 = motors.motor(5,6,12,13)

    contr = motors.motorcontroller(motors.motorarray([motor1,motor2,motor3,motor4,motor5]))
    contr.jank()

    while True:
        #getAnswers 
        answers = (1/5,1/8,1/9)

        #Change Lights
        led.colorCycle(stress,answers[3])
        stress = answers[3]

        #Change Height
        contr.setHeights([maxheight*answers[0]+minheight])

        #Change Harmony
        """""
        h = [0]*5
        for i in range(5):
            h[i] = harmonHeights[i]+answers[1]*chaosHeights[i]
        contr.changeHeights(h)
        """

def adjustHeights():
    marray = motors.motorarray([motor1,motor2,motor3,motor4,motor5])   
    print("enter -1 to exit")
    while True:   
        x = float(input("enter motor number: "))
        y = float(input("enter rotation amount: "))
        if x == -1:
            break
        else: 
            if y > 0:
                marray.arr[x].forward(y)
            else:
                marray.arr[x].backward(abs(y))

    GPIO.cleanup()


contr.jank()
contr.changeHeights([10]*5)
contr.changeHeights([-2,-1,3,2.5,-5])
contr.zeroHeights()
#adjustHeights()


""""
led = leds.ledcontroller()
led.pixels.fill((0,0,0))
time.sleep(2)
led.colorRows(0)
led.colorCycle(0,1)
time.sleep(2)
led.pixels.fill((0,0,0))
GPIO.cleanup()
"""


            
