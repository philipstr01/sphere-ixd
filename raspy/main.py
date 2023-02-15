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

motor4 = motors.motor(2,3,4,14)
motor3 = motors.motor(15,17,19,27)
motor1 = motors.motor(22,23,24,10)
motor2 = motors.motor(9,11,8,7)
motor0 = motors.motor(5,6,12,13)
marray = motors.motorarray([motor0,motor1,motor2,motor3,motor4])   
contr = motors.motorcontroller(marray)

led = leds.ledcontroller()
led.pixels.fill((0,0,0))

#main function
def main():
    minheight = 2
    maxheight = 8 + minheight

    chaosHeights = [2,0.5,5,2.5,2] #[0.4,0.1,1,0.5,0.2]
    harmonHeights = [2,4.45,0,4.45,2] #[2.5,4.45,0,4.45,2.5]

    stress = 0

    contr.jank()

    compTime = datetime.now()
    prevanswers = (2,2,2)
    n = 0
    while True:
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
        if answers == prevanswers:
            time.sleep(5)
            continue

        if answers == (-1,-1,-1):
            print("Entering null mode!")
            contr.zeroHeights()
            led.pixels.fill((0,0,0))
            stess = 0
            print("Null mode sleep... 5s")
            time.sleep(5)
            continue
        
        #Change Lights
        print("Changing Lights:"+str(answers[1]))
        led.colorCycle(stress,answers[1])
        stress = answers[1]

        #Change Height
        print("Changing Height:"+str(answers[0]))
        contr.jank()
        contr.setHeights([maxheight*answers[0]+minheight]*5)

        print("Controller Heights:")
        print(contr.heights)

        #Change Harmony
        print("Changing Harmony: "+str(answers[2]))
        h = [0]*5
        for i in range(5):
            h[i] = harmonHeights[i]+answers[2]*chaosHeights[i]

        print("Controller Heights:")
        print(contr.heights)

        contr.jank()
        contr.changeHeights(h)
        time.sleep(10)
        #n += 1
    
    print("Controller Heights:")
    print(contr.heights)
    print("Finished main!")
    time.sleep(10)
    contr.zeroHeights()
    led.pixels.fill((0,0,0))


contr.adjustHeights()
main()

            
