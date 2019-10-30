import re

line = 'Start   blabla End'

text = '''
prefix
Start
blabla
End
postfix
'''

regex = r'^Start[\d\D]*End$'
m = re.search(regex, line)
if (m):
    print('line')

m = re.search(regex, text)
if (m):
    print('text')

print('-' * 10)

m = re.search(regex, line, re.MULTILINE)
if (m):
    print('line')

m = re.search(regex, text, re.MULTILINE)
if (m):
    print('text')
