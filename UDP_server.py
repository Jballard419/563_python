import socket
import sys
UDP_IP="127.0.0.1"
UDP_PORT = sys.argv[1]
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((UDP_IP,UDP_PORT))

while 1:
    data, addr =sock.recvfrom(1024)
    print "received message:", data
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.sendto(data.upper(), (addr, UDP_PORT))
    
