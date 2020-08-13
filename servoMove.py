from gpiozero import AngularServo
from time import sleep
#servo = AngularServo(2, min_angle=-180, max_angle=180)

#angleReal = 150 # assuming this is center for the gun

servo = AngularServo(2, min_angle=-180, max_angle=180)

angleReal = 150 # assuming this is center for the gun
for x in range(2):
    servo.angle = 160
    sleep(.5)
for x in range(2):
    servo.angle = -160
    sleep(.5)
def turnleft():
    servo.angle = (angleReal - 1)

def turnright():
    servo.angle = (angleReal + 1)



