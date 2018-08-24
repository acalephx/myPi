import socket
import time

HOST = '192.168.2.102'
PORT = 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('b')
sock.connect((HOST, PORT))
# print(b'a')
sock.send(b'a')
# sock.send(b'b')
while 1:
    time.sleep(0.5)
    buf = sock.recv(1024).decode()
    if buf:
        print(buf)


sock.close()

