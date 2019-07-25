__Author__ = "noduez"

from socket import *

HOST = 'localhost'
PORT = 2051
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        continue
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    print(data.decode('utf-8'))

tcpCliSock.close()