import xml.dom.minidom

file = 'examples/xml/data.xml'

dom = xml.dom.minidom.parse(file)

root = dom.firstChild
print(root.tagName)

print('')

for node in root.childNodes:
    if node.nodeType != node.TEXT_NODE:
        print('name: ', node.tagName)
        print('id: ', node.getAttribute('id'))

print('')

emails = dom.getElementsByTagName("email")
for e in emails:
    print('email', e.getAttribute('id'), e.firstChild.data)

