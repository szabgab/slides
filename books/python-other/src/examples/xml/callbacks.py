import xml.parsers.expat
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

file = sys.argv[1]


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
