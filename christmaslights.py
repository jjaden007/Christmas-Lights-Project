#Date Last Updated: Jan 19, 2025
#Developer: Jaden Singh 
#description: This Python script controls four LEDs using a button on a Raspberry Pi. 
# Pressing the button cycles through four different lighting modes, each with a unique blinking pattern. 
# The **gpiozero** library is used to handle the button and LED interactions. 
# The script continuously checks the current mode and runs the corresponding lighting function until the mode is changed.

from gpiozero import LED, Button
import time

button = Button(17)
greenled = LED(27)
redled = LED(21)
blueled = LED(12)
blueled2 = LED(16)
mode_check = ""
current_mode = 1  


def switch_mode():
    global current_mode
    current_mode += 1  
    if current_mode > 4:  
        current_mode = 1


button.when_pressed = switch_mode

def mode1():
    while current_mode == 1:  
        greenled.on()
        redled.on()
        blueled.on()
        blueled2.on()
        time.sleep(1.5)
        greenled.off()
        redled.off()
        blueled.off()
        blueled2.off()
        time.sleep(1.5)

def mode2():
    while current_mode == 2:  
        greenled.on()
        redled.on()
        blueled.on()
        blueled2.on()
        time.sleep(0.2)
        greenled.off()
        redled.off()
        blueled.off()
        blueled2.off()
        time.sleep(0.2)

def mode3():
    while current_mode == 3:  
        greenled.on()
        time.sleep(0.5)
        greenled.off()
        redled.on()
        time.sleep(0.5)
        redled.off()
        blueled.on()
        time.sleep(0.5)
        blueled.off()
        blueled2.on()
        time.sleep(0.5)
        blueled2.off()

def mode4():
    while current_mode == 4:  
        greenled.on()
        blueled.on()
        time.sleep(0.5)
        greenled.off()
        blueled.off()
        redled.on()
        blueled2.on()
        time.sleep(0.5)
        redled.off()
        blueled2.off()

def main():
    def main():
    global mode_check
    while True:
        
        button.wait_for_press()
        
        if mode_check == "":
            mode1()
            mode_check = "mode1"
            print("mode1")
        elif mode_check == "mode1":
            mode2() 
            mode_check = "mode2"
            print("mode2")
        elif mode_check == "mode2":
            mode3()
            mode_check = "mode3"
        elif mode_check == "mode3":
            mode4()
            mode_check = "mode4"
        elif mode_check == "mode4":
            greenled.off()
            redled.off()
            blueled.off()
            blueled2.off()
            mode_check = ""
    global current_mode
    while True:
        if current_mode == 1:
            mode1()
        elif current_mode == 2:
            mode2()
        elif current_mode == 3:
            mode3()
        elif current_mode == 4:
            mode4()

if __name__ == "__main__":
    main()


       
main()
