import RPi.GPIO as GPIO
import time

import os
from os import listdir
from os.path import isfile, join
import random

mypath = "/home/pi/soundbox/sounds"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def play_sound(channel):
    index = random.randint(0, len(onlyfiles)-1)
    selected = onlyfiles[index]
    os.system('aplay '+mypath+'/'+selected)
    print('Button Pressed')
    time.sleep(0.2)

GPIO.add_event_detect(18, GPIO.FALLING, callback=play_sound, bouncetime=300)  

try:
    while True:
        GPIO.wait_for_edge(18, GPIO.RISING)  
        

except KeyboardInterrupt:  

    GPIO.cleanup()    
GPIO.cleanup()
#while True:
#    input_state = GPIO.input(18)
#    if input_state == False:
