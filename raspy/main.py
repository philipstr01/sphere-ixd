import base_functions
import motors
import RPi.GPIO as GPIO
import time

#base_functions.download_write_responses()
#df = base_functions.getsurveyDataframe()
#mysurvey = base_functions.getSurveyObject()

#Motor Test script,
GPIO.setmode(GPIO.BCM)
motor1 = motors.motor(2,3,4,14)
motor2 = motors.motor(15,17,18,27)
motor3 = motors.motor(22,23,24,10)
motor4 = motors.motor(9,11,8,7)
motor5 = motors.motor(5,6,12,13)
motor1.forward(0.1)
motor2.forward(0.1)
motor3.forward(0.1)
motor4.forward(0.1)
motor5.forward(0.1)
#motor1.backward(1)
GPIO.cleanup()
