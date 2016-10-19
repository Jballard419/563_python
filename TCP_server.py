import socket
import sys
TCP_IP = '127.0.0.1'
TCP_PORT = sys.agrv[1];
BUFFER_SIZE= 1024
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind((TCP_IP,TCP_PORT))
while 1:
    s.listen(1)
    conn,addr=s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data.upper());
    conn.close() #fin
