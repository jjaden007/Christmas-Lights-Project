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
""""
def mode2()
    while true:
    button.wait_for_press()
    print('THE BUTTON WAS PRESSED')
    if on_off==False:
        greenled.on(1.5)
        redled.on(1.5)
        blueled.on(1.5)
        blueled2.on(1.5)
        greenled.off(1.5)
        redled.off(1.5)
        blueled.off(1.5)
        blueled2.off(1.5)

mode1()


while (True):
    button.wait_for_press()
    print('THE BUTTON WAS PRESSED')
    if on_off==False:
        greenled.on()
        redled.on()
        blueled.on()
        blueled2.on()
        time.sleep(1.5)
        on_off=True
        print ('LED is now on')
    
    elif on_off==True:
        greenled.off()
        redled.off()
        blueled.off()
        blueled2.off()
        time.sleep(1.5)
        print('LED is now off')
        on_off=False
"""