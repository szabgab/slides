import re

line = 'Before <div>content</div> After'

text = '''
Before
<div>
content
</div>
After
'''

match = re.search(r'<div>.*</div>', line)
if match:
    print(f"line '{match.group(0)}'");

match = re.search(r'<div>.*</div>', text)
if match:
    print(f"text '{match.group(0)}'");

print('-' * 10)

match = re.search(r'<div>.*</div>', line, re.DOTALL)
if match:
    print(f"line '{match.group(0)}'");

match = re.search(r'<div>.*</div>', text, re.DOTALL)
if match:
    print(f"text '{match.group(0)}'");

