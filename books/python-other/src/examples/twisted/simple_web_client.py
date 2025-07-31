from twisted.internet import reactor
from twisted.web.client import getPage
import sys

def printPage(result):
    print("Page")
    print('Size of the returned page is {}'.format(len(result)))

def printError(error):
    print("Error")
    print(f"Error: {error}")
    #sys.stderr.write(error)

def stop(result):
    print('stop')
    reactor.stop()

if (len(sys.argv) != 2):
    sys.stderr.write("Usage: python " + sys.argv[0] + " <URL>\n")
    exit(1)

d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)

reactor.run()

# getPage(sys.argv[1], method='POST', postdata="My test data").
