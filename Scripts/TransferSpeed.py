from bluetooth import *
from PyOBEX.client import Client
from pprint import pprint
import time
import os, sys
  
services = find_service(uuid='94f39d29-7d6d-437d-973b-fba39e49d4ee',address='54:14:F3:B6:6E:B6')
if len(services) == 0:
    print("Couldn't find service")
    sys.exit(0)
else:
    pprint("Found service")
first_match = services[0]
port = first_match["port"]
name = first_match["name"]

print("Connecting to \"%s\" on %s" % (name, port))
def connect(port):
    addr = "54:14:F3:B6:6E:B6"
    sock = BluetoothSocket(RFCOMM)
    #while 1:
    t1 = time.time()
    sock.connect((addr, port))
    while True:
        data = input()
        if len(data) == 0: break
        elif len(data) == 1:
            send_file(sock, "/home/pi/Documents/CubeSat/chonkers.jpg", 18)
        #sock.send(data)
    
    t2 = time.time()
    
    print("time taken {}".format(t2-t1))
    sock.close()
def send_file(sock, file_path, size = 1024):
    file = open(file_path, "rb")
    sock.send(time.ctime())
    packet = 1
    print(file_path, "is", os.path.getsize(file_path), "starts @", time.ctime())
    while(packet):
        packet = file.read(1024)
        sock.send(packet)
    print("Send @:", time.ctime())
    isFileSent = True
    file.close()
    sock.send("End file transfer.")
connect(port)
