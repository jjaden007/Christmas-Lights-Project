#Date Last Updated: Jan 19, 2025
#Developer: Jaden Singh
#description: Button on/off switch
from gpiozero import Button
from gpiozero import LED
import time

button = Button(19)
led = LED(26)
on_off=False
while (True):
    button.wait_for_press()
    print('THE BUTTON WAS PRESSED')
    if on_off==False:
        led.on()
        time.sleep(1.5)
        on_off=True
        print ('LED is now on')
    
    elif on_off==True:
        led.off()
        time.sleep(1.5)
        print('LED is now off')
        on_off=False
    
   



