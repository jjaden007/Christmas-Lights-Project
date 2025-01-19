#Date Last Updated: Jan 19, 2025
#Developer: Jaden Singh 
#description: This Python script uses the **gpiozero** library to detect button presses on a Raspberry Pi. 
# It initializes a button on GPIO pin 17 and continuously waits for it to be pressed. 
# When pressed, it prints **"THE BUTTON WAS PRESSED!"** and then pauses for 1 second before checking again.

from gpiozero import Button
import time

button = Button(17)
while (True):
    button.wait_for_press()
    print ('THE BUTTON WAS PRESSED!')
    time.sleep(1)