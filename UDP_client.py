import socket
import sys
UDP_IP = sys.argv[1]
UDP_IPold="127.0.0.1"
UDP_PORT = sys.argv[2]
sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((UDP_IPold,UDP_PORT))
while 1:
    MESSAGE = input("Entire MESSAGE:")
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, addr =sock.recvfrom(1024)
    print "received message:", data
