import socket
import sys
UDP_IP="127.0.0.1"
UDP_PORT =int( sys.argv[1])
sock= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while 1:
    data, addr =sock.recvfrom(1024)
    print "received message:", data
   
    sock.sendto(data.upper(), addr )

    
