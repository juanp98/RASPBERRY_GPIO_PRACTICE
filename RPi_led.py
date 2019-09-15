from gpiozero import LED
from time import sleep

while True:
    ledRojo = LED(13)

    ledRojo.on()
    sleep(3)
    ledRojo.off()

   



