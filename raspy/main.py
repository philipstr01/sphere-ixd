import base_functions
import motors
import RPi.GPIO as GPIO
import time

#base_functions.download_write_responses()
#df = base_functions.getsurveyDataframe()
#mysurvey = base_functions.getSurveyObject()

#Motor Test script

motor1 = motors.motor(13,15,16,18)

i = 0
while i < 10:
  motor1.forward(1,1)
  i += 1
