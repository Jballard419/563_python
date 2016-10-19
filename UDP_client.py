import socket
import sys
UDP_IP = sys.argv[1]
UDP_IPold="127.0.0.1"

UDP_PORT =int( sys.argv[2])
s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while 1:
    MESSAGE = input("Entire MESSAGE:")
    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, addr =s.recvfrom(1024)
    print "received message:", data
