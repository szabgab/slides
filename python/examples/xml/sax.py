import xml.sax
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

file = sys.argv[1]

class EventHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print('start', (name, attrs._attrs))

    def characters(self, text):
        if not text.isspace():
            print('text', text)

    def endElement(self, name):
        print('end', name)


xml.sax.parse(file, EventHandler())

