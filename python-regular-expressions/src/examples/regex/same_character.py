import re

strings = [
    'banana',
    'apple',
    'infinite loop',
]

for line in strings:
    match = re.search(r'(.)\1', line)
    if match:
        print(match.group(0), 'matched in', line)
        print(match.group(1))
