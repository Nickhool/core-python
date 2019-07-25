__Author__ = "noduez"

from socket import *
from time import ctime
import os
import re

HOST = ""
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
responsedic = {'date': ctime(), 'os': os.name, 'ls': str(os.listdir(os.curdir))}

while True:
    print
    "Waiting for connect..."
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        findre = re.match(r'ls dir\((.+)\)', str(data))
        data_str = data.decode('utf-8')
        if not data:
            break
        elif responsedic.get(data_str):
            tcpCliSock.send(responsedic[data_str].encode('utf-8'))
        elif findre:
            print(os.listdir(findre.group(1)))
            tcpCliSock.send(str(os.listdir(findre.group(1))))
        else:
            tcpCliSock.send(data)
    tcpCliSock.close()
tcpCliSock.close()