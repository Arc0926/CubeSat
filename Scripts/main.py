import adafruit_bno055
import time
import os
import board
import busio
from picamera import PiCamera
import numpy as np
import sys
import threading
from bluetooth import *
from ATTITUD import *
from plastic_detection import *
from GIT_TRANSFER import *
from TransferSpeed import *

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

camera = PiCamera()

addr = "54:14:F3:B6:6E:B6"
uuid = '94f39d29-7d6d-437d-973b-fba39e49d4ee'
def capture():
    print("Begin moving camera.")
    while True:
        time.sleep(10)
        t = time.ctime().replace(":", " ")     # current time string
        imgname = ('/home/pi/Documents/CubeSat/Images/%s.jpg' % (t)) #change directory to your folder
        camera.capture(imgname)
        plastic_detection('Images/%s.jpg' % (t))
        connect(sock, addr, uuid)
        send_file(sock, "/home/pi/Documents/CubeSat/Images/Masks/mask.jpg", 1024)

sock = BluetoothSocket(RFCOMM)
capture()
