import re

line = 'There is a phone number 12345 in this row and an age: 23'

match = re.search(r'((\w+) (\w+)): (\d+)', line)
if match:
    print(match.group(0))  # an age: 23
    print(match.group(1))  # an age
    print(match.group(2))  # an
    print(match.group(3))  # age
    print(match.group(4))  # 23

    print(match.groups())  # ('an age', 'an', 'age', '23')
    print(len(match.groups()))  # 4
