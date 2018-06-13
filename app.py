import serial
import os
from os import listdir
from os.path import isfile, join
mypath = "sounds"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

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
        os.system('aplay piano2.wav')

s.close()