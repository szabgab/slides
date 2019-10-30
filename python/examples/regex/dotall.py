import re

line = 'Before <div>content</div> After'

text = '''
Before
<div>
content
</div>
After
'''

if (re.search(r'<div>.*</div>', line)):
    print('line');
if (re.search(r'<div>.*</div>', text)):
    print('text');

print('-' * 10)

if (re.search(r'<div>.*</div>', line, re.DOTALL)):
    print('line');
if (re.search(r'<div>.*</div>', text, re.DOTALL)):
    print('text');
