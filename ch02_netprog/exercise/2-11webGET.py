__Author__ = "noduez"

from socket import *
HOST = 'www.bilibili.com'
PORT = 80
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
tcpCliSock.send('GET/\n'.encode('utf-8'))
data = tcpCliSock.recv(BUFSIZ)
with open(r"webpage.txt",'w') as f:
    f.write(data.decode('utf-8'))