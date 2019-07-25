__Author__ = "noduez"

from socket import *

DefaultHOST = 'localhost'
DefaultPORT = 1236
BUFSIZ = 1024


def GetAddr():
    Host = input("Please input host:")
    Port = input("Please input port:")
    return Host, int(Port)


Host, Port = GetAddr()

if not Host:
    Host = DefaultHOST
if not Port:
    Port = DefaultPORT

ADDR = (Host, Port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    print(data)

tcpCliSock.close()