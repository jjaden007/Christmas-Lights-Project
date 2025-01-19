#Date Last Updated: Jan 19, 2025
#Developer: Jaden Singh  
#description: This Python script uses the **gpiozero** library to control an LED on a Raspberry Pi. 
# It continuously turns the LED on for **1.5 seconds**, then off for **1.5 seconds**, creating a blinking effect.
from gpiozero import LED
import time

led = LED(17)
while(True):
    led.on()
    time.sleep(1.5)
    led.off()
    time.sleep(1.5)
    