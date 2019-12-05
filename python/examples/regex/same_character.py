import re

strings = [
    'banana',
    'apple',
]

for s in strings:
    match = re.search(r'(.)\1', s)
    if match:
        print(match.group(0), 'matched in', s)
        print(match.group(1))
