import base_functions
import motors
import RPi.GPIO as GPIO
import time
import neopixel
import board
#import leds

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
contr = motors.motorcontroller(motors.motorarray([motor1,motor2,motor3,motor4,motor5]))
contr.jank()


pixels = neopixel.NeoPixel(board.D18,80)
pixels.fill((0,0,0))
n = 0
while n<=80:
    #pixels[n] = (255,0,0)
    n += 1
    print(n)
    contr.changeHeights([0.5,0.5,0.5,0.5,0.5])
    time.sleep(0.5)
    
pixels.fill((0,0,0))
GPIO.cleanup()
