import socket
import time
import sys

HOST = '192.168.2.102'
PORT = 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('b')
# sock.connect((HOST, PORT))
# # print(b'a')
# sock.send(b'a')
# # sock.send(b'b')
# while 1:
#     time.sleep(0.5)
#     buf = sock.recv(1024).decode()
#     if buf:
#         print(buf)
#
#
# sock.close()
while True:
    try:
        print("Connecting to server @ %s:%d..." % (HOST, PORT))
        sock.connect((HOST, PORT))
        break
    except Exception:
        print("Can't connect to server,try it latter!")
        time.sleep(1)
        continue
print("Please input 1 or 0 to turn on/off the led!")
while True:
    try:
        data = sock.recv(512).decode()
        if len(data) > 0:
            print("Received: %s" % data)
            command = raw_input()
            sock.send(command)
            time.sleep(0.3)
            continue
    except Exception:
        sock.close()
        sock = None
        sys.exit(1)
