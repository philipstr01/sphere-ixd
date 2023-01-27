import base_functions
import RPi.GPIO as GPIO
import time

base_functions.download_write_responses()
df = base_functions.getsurveyDataframe()

question_columns = ["G01Q01","G01Q02","G01Q03"]

"""
butstate = 0
count = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN)

while True:
    if count > 2:
        count = 0
    for i in range(df[question_columns[count]].mean().round(0)):
        GPIO.output(16,True)
        time.sleep(100)
        GPIO.output(16,False)
        time.sleep(100)
    if GPIO.input(18) == 0:
        if butstate == 0:
            butstate = 1
            count += 1
        else:
            butstate == 0
"""
print("hello world")
GPIO.cleanup()
