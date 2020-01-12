from twisted.internet import reactor,protocol
import sys

if len(sys.argv) < 2:
    exit("Usage: {sys.argv[0]} TEXT")

message = sys.argv[1]
port = 8000

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(message.encode('utf8'))

    def dataReceived(self, data):
        print(f"Server said: {data}")
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("connection failed")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("connection lost")
        reactor.stop()

reactor.connectTCP("localhost", port, EchoFactory())
reactor.run()
