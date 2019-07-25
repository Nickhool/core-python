__Author__ = "noduez"
# 创建 Twisted Reactor TCP 服务器

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connect from:', clnt)
    def dataReceived(self, data):
        self.transport.write('[%s] %s'.encode('utf-8') % (bytes(ctime(), 'utf-8'), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()