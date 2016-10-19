import socket
import sys
TCP_IP = sys.argv[1]
TCP_PORT = sys.argv[2]
BUFFER_SIZE= 1024

while 1:

    MESSAGE = input("Entire MESSAGE:")
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    S.connect((TCP_IP,TCP_PORT))
    s.send(MESSAGE)
    data= s.recv(BUFFER_SIZE)
    s.close()
    Print "received data:", data
