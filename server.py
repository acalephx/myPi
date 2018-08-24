import socket
import time

HOST = '192.168.2.102'
PORT = 8002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

while 1:
    try:
        connection, address = sock.accept()
        # connection.settimeout(10)
        buf = connection.recv(1024)
        if buf == 'a':
            connection.send(b'Start!')
            print('Start')
            print(buf)
            while buf != 'b':
                print('working')
                connection.send(b'myData')
                time.sleep(0.5)
                # buf = connection.recv(1024)
        elif buf == 'b':
            connection.send(b'Stop!')
            print('Stop')
        else:
            connection.send(b'please go out!')
    except socket.timeout:
        print('time out')
connection.close()
sock.close()
