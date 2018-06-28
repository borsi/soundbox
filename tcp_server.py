#!/usr/bin/env python

import socket

import os

import winsound

from os import listdir
from os.path import isfile, join
import random

mypath = "sounds"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
s.close()
print('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE).decode()
    if(data == 'play'):
        print(onlyfiles)
        index = random.randint(0, len(onlyfiles)-1)
        selected = onlyfiles[index]
        winsound.PlaySound(mypath+'/'+selected, winsound.SND_FILENAME   )
    if(data == 'close'):
        conn.close()
        break
    if data: 
        print("received data:", data)
        conn.send(data.upper().encode())  # echo