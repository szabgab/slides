import re

strings = [
    'apple pie',
    'banana pie',
    'apple'
]

for s in strings:
    match = re.search(r'(apple|banana) pie', s)
    if match:
        print('Matched in', s)
