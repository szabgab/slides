import xml.sax
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

file = sys.argv[1]

class EventHandler(xml.sax.ContentHandler):
    def __init__(self, c):
        self.path = []
        self.collector = c

    def startElement(self, name, attrs):
        self.path.append({ 'name' : name, 'attr' : attrs._attrs })

    def characters(self, text):
        self.path[-1]['text'] = text

    def endElement(self, name):
        element = self.path.pop()
        print('End name: ', name)
        if element['name'] == 'email':
            collector.append(element)

collector = []
xml.sax.parse(file, EventHandler(collector))
print(collector)
