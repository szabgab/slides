from twisted.internet import protocol,reactor

port = 8000

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        text = data.decode('utf8')
        print(f"Received: {text}")
        self.transport.write("You said: {}".format(text).encode('utf8'))

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

print(f"Listening on port {port}")
reactor.listenTCP(port, EchoFactory())
reactor.run()
