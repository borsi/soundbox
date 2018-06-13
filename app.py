import serial
import os
from os import listdir
from os.path import isfile, join
import random

mypath = "sounds"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


PORT = "/dev/ttyACM0"
BAUD =  115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    data = s.readline().decode("UTF-8")
    string = str(data).split(" ")
    if(string[0] == "A"):
        print(onlyfiles)
        index = random.randint(0, len(onlyfiles)-1)
        selected = onlyfiles[index]
        os.system('aplay '+mypath+'/'+selected)

s.close()
