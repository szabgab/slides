import xml.sax

file = 'examples/xml/data.xml'

class EventHandler(xml.sax.ContentHandler):
    def __init__(self,target):
        self.target = target
    def startElement(self,name,attrs):
        self.target.send(('start',(name,attrs._attrs)))
    def characters(self,text):
        self.target.send(('text',text))
    def endElement(self,name):
        self.target.send(('end',name))

def printer():
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        cr.next()
        return cr
    return start

# example use
if __name__ == '__main__':
    @coroutine
    def printer():
        while True:
            event = (yield)
            print(event)

    xml.sax.parse(file, EventHandler(printer()))



