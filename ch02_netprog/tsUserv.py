__Author__ = "noduez"
# UDP 时间戳服务器

from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)


while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s'.encode('utf-8') % (
        bytes(ctime(), 'utf-8'), data), addr)
    print('...received form and return to:', addr)

udpSerSock.close()