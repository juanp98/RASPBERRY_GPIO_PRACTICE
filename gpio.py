from gpiozero import LED
from time import sleep

ledAmarillo = LED(27)
ledVerde = LED(17)
ledRojo = LED(22)

while True:
    ledVerde.on()
    sleep(4)
    ledVerde.off()

    ledVerde.blink(0.2,0.2)
    sleep(3)
    ledVerde.off()

    ledAmarillo.on()
    sleep(2)
    ledAmarillo.off()

    ledRojo.on()
    sleep(3)
    ledRojo.off()
