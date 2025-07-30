import xml.etree.ElementTree as ET
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

file = sys.argv[1]

tree = ET.parse(file)
root = tree.getroot()
print(root.tag)

for p in root.iter('person'):
    print(p.attrib)

print('')

for p in root.iter('email'):
    print(p.attrib, p.text)

print('')

elements = tree.findall(".//*[@id='home']")
for e in elements:
    print(e.tag, e.attrib)
