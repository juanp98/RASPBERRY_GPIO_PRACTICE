import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

velocity = GPIO.PWM(11, 100)
velocity.start(0)

while True:
    for vel in range(0,100):
        velocity.ChangeDutyCycle(vel)
        sleep(0.02)
    for vel in range(100,0,-1):
        velocity.ChangeDutyCycle(vel)
        sleep(0.02)