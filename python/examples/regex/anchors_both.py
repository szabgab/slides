import re

strings = [
    "123",
    "hello 456 world",
]

for line in strings:
    if re.search(r'\d+', line):
        print(line)

print('---')

for line in strings:
    if re.search(r'^\d+$', line):
        print(line)


