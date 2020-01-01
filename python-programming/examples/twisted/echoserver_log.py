from twisted.internet import protocol,reactor

class Echo(protocol.Protocol):
  def dataReceived(self, data):
    print "Received:", data
    self.transport.write(data)

class EchoFactory(protocol.Factory):
  def buildProtocol(self, addr):
    print "Contection established with", addr
    return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()
