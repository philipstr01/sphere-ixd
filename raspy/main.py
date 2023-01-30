import base_functions
import motors
import RPi.GPIO as GPIO
import time

#base_functions.download_write_responses()
#df = base_functions.getsurveyDataframe()
#mysurvey = base_functions.getSurveyObject()

#Motor Test script

motor1 = motors.motor(13,15,16,18)

motor1.forward(1)
motor1.backward(1)
GPIO.cleanup()
