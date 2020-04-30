from gpiozero import LED
from time import sleep
from gpiozero import PWMLED
from signal import pause
import random
import os

sleep (10)

os.system('mpg321 /home/pi/Documents/tardis.mp3 &')

def flashone():
    led = LED(4)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        
    
def flashtwo():
    led = PWMLED(4)
    led.pulse()
    pause()
    
    
def flashthree():
    led = LED(4)
    led.on()
    pause()
    
def flashfour():
    led = LED(4)

    while True:
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.3)
        
  
       
flash = [flashone, flashtwo, flashthree, flashfour]
random.choice(flash)()

