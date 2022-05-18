"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

from bluetooth import *

hostMACAddress = '54:14:F3:B6:6E:B6' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 4
backlog = 1
size = 1024
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

def get_file(client_sock, file_path, size = 1024):
    """
    Collects arriving packets
    """
    absolutepath = os.path.abspath(__file__)
    parentDirectory = os.path.dirname(os.path.dirname(absolutepath))
    name = client_sock.recv(size)
    relativePath = "/Images/" + name.decode('utf-8') + ".jpg"
    fileName = os.path.join(parentDirectory, relativePath).replace("\\","/")
    file = open(fileName, 'wb')
    packet = "1"
    print("entering packet loop")
    counter = 0
    while packet:
        packet = client_sock.recv(size)
        try:
            if packet.decode('utf-8') == "End file transfer.":
                print("closing file")
                file.close()
                print("counter:", counter)
        except:
            print("writing jpg")
            counter = counter + 1
            file.write(packet)

    isFileGot= True
    file.close()
    print ("File GOT")
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind((hostMACAddress, port))
server_sock.listen(backlog)




advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

client_sock, client_info = server_sock.accept()

get_file(client_sock, 1, 1024)


'''    
try:
    while 1:
        get_file(1, 18)

except:	
    print("Closing socket")
    client_sock.close()
    server_sock.close()
    
'''