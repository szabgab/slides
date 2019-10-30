import xml.sax

file = 'examples/xml/data.xml'


class EventHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print('start', (name, attrs._attrs))

    def characters(self, text):
        if not text.isspace():
            print('text', text)

    def endElement(self, name):
        print('end', name)


xml.sax.parse(file, EventHandler())

