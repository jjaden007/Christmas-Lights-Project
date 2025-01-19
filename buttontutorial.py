from gpiozero import Button
import time

button = Button(17)
while (True):
    button.wait_for_press()
    print ('THE BUTTON WAS PRESSED!')
    time.sleep(1)