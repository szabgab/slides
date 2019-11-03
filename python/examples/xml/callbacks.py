import xml.parsers.expat

file = 'examples/xml/data.xml'


def start_element(name, attrs):
    print('Start element: {} {}'.format(name, attrs))


def end_element(name):
    print('End element: {}'.format(name))


def char_data(data):
    print('Character data: {}'.format(repr(data)))


p = xml.parsers.expat.ParserCreate()

p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

p.ParseFile(open(file, 'rb'))

print('done')
