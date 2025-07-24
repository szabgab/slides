import re

s = 'Python'

if (re.search('python', s)):
    print('python matched')

if (re.search('python', s, re.IGNORECASE)):
    print('python matched with IGNORECASE')
