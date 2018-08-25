import socket
import time

HOST = '192.168.2.102'
PORT = 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
connection, (HOST_IP, HOST_PORT) = sock.accept()
print("Connection accepted from %s." % HOST_IP)
connection.send(b'Welcome to RPi TCP server!')
while 1:
    try:
        buf = connection.recv(1024)
        if len(buf) > 0:
            if buf == '1':
                connection.send(b'Start!')
                print('Start')
                print('working')
                connection.send(b'myData')
                time.sleep(0.5)
            elif buf == '0':
                connection.send(b'Stop!')
                print('Stop')
            time.sleep(0.5)
            continue
    except Exception:
        sock.close()
        # sys.exit(1)
# connection.close()
# sock.close()
