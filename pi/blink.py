# Added comment
import gpiozero
import time

led = gpiozero.LED(4)
n=1

while True:
   led.on()
   time.sleep(.1)
   led.off()
   time.sleep(.1)
   n=n+1
