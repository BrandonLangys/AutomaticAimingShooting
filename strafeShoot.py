from gpiozero import AngularServo
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

servo = AngularServo(2, min_angle=-180, max_angle=180)

angleReal = 150 # assuming this is center for the gun

for x in range(25):
    servo.angle = angleReal + 1
    sleep(.05)
    GPIO.output(4, GPIO.HIGH)
    sleep(.03)
    GPIO.output(4, GPIO.LOW)
def turnleft():
    servo.angle = (angleReal - 1)

def turnright():
    servo.angle = (angleReal + 1)

def shootGun():
    for i in range(15):
        GPIO.output(4, GPIO.HIGH)
        sleep(.03)
        GPIO.output(4, GPIO.LOW)