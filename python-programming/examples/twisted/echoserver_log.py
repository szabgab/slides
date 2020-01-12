from twisted.internet import protocol,reactor

port = 8000

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print("Received: {}".format(data))
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        print(f"Contection established with {addr}")
        return Echo()

print(f"Started to listen on port {port}")
reactor.listenTCP(port, EchoFactory())
reactor.run()
