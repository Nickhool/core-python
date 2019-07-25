__Author__ = "noduez"
# 创建 Twisted Reactor TCP 客户端

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567

class TSCIntProtocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('...sending %s...' % data)
            self.transport.write(data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()

class TSCIntFactory(protocol.ClientFactory):
    protocol = TSCIntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSCIntFactory())
reactor.run()