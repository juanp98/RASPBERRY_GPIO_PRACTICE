from gpiozero import AngularServo
from time import sleep

servo1 = AngularServo(10,min_angle=-170,max_angle=170)

while True:
    servo1.angle = -170
    sleep(0.5)
    servo1.angle = 150
    sleep(0.5)