import base_functions
import motors
import RPi.GPIO as GPIO
import time

#base_functions.download_write_responses()
#df = base_functions.getsurveyDataframe()
#mysurvey = base_functions.getSurveyObject()

#Motor Test script,
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor1 = motors.motor(2,3,4,14)
motor2 = motors.motor(15,17,18,27)
motor3 = motors.motor(22,23,24,10)
motor4 = motors.motor(9,11,8,7)
motor5 = motors.motor(5,6,12,13)
contr = motors.motorcontroller(motors.motorarray({motor1:False,motor2:False,motor3:True,motor4:True,motor5:True}))
contr.updateheights([3.5,3,2.5,2,1.5])
GPIO.cleanup()
