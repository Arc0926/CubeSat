from bluetooth import *
from PyOBEX.client import Client
from pprint import pprint
import time
import os, sys
send_photo = False


def start_send():
    send_photo = True


def connect(sock, addr, uuid):
    services = find_service(uuid,addr)
    if len(services) == 0:
        print("Couldn't find service")
        sys.exit(0)
    else:
        pprint("Found Service")
    first_match = services[0]
    port = first_match["port"]
    t1 = time.time()
    sock.connect((addr, port))
    #sock.close()
def send_file(sock, file_path, size = 1024):
    sock.send("Start file transfer.")
    file = open(file_path, "rb")
    packet = 1
    print(file_path, "is", os.path.getsize(file_path), "starts @", time.ctime())
    while(packet):
        packet = file.read(size)
        sock.send(packet)
    print("Sent @:", time.ctime())
    file.close()
    sock.send("End file transfer.")

