import base_functions
import motors
import RPi.GPIO as GPIO
import time
import leds
import datetime
from datetime import datetime, timedelta

#Motor Test script
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motor1 = motors.motor(2,3,4,14)
motor2 = motors.motor(15,17,19,27)
motor3 = motors.motor(22,23,24,10)
motor4 = motors.motor(9,11,8,7)
motor5 = motors.motor(5,6,12,13)
marray = motors.motorarray([motor1,motor2,motor3,motor4,motor5])   
contr = motors.motorcontroller(marray)

led = leds.ledcontroller()
led.pixels.fill((0,0,0))

#main function
def main():
    minheight = 1
    maxheight = 9 + minheight

    chaosHeights = [0.4,0.1,1,0.5,0.2]
    harmonHeights = [2.5,4.45,0,4.45,2.5]

    stress = 0

    contr = motors.motorcontroller(motors.motorarray([motor1,motor2,motor3,motor4,motor5]))
    contr.jank()

    compTime = datetime.now()

    n = 0
    while n<1:
        #Check Time
        print("Checking Time:")
        if datetime.now()-compTime >= timedelta(minutes=30):
            compTime = datetime.now()
        print("compTime = "+str(compTime))

        #getAnswers 
        print("Getting answers:")
        base_functions.download_write_responses()
        df = base_functions.getsurveyDataframe()
        answers = base_functions.calcMeans(df,compTime)
        print("Answers = "+str(answers))
        if answers == (-1,-1,-1):
            print("Entering null mode!")
            contr.zeroHeights()
            led.pixels.fill(0,0,0)
            continue
        
        #Change Lights
        print("Changing Lights:")
        led.colorCycle(stress,answers[1])
        stress = answers[1]

        #Change Height
        print("Changing Height:")
        contr.setHeights([maxheight*answers[0]+minheight]*5)

        #Change Harmony
        print("Changing Harmony")
        """""
        h = [0]*5
        for i in range(5):
            h[i] = harmonHeights[i]+answers[2]*chaosHeights[i]
        contr.changeHeights(h)
        """
        n += 1
    contr.zeroHeights()


#contr.adjustHeights()
main()

            
