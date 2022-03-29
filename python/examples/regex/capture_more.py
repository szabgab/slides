import re

line = 'There is a phone number 12345 in this row and an age: 23'

match = re.search(r'(\w+) (\w+): (\d+)', line)
if match:
    print(match.group(0))  # an age: 23  the full match
    print(match.group(1))  # an          the 1st group of parentheses
    print(match.group(2))  # age         the 2nd group of parentheses
    print(match.group(3))  # 23          the 3rd group of parentheses

    # print(match.group(4))  # IndexError: no such group
    print(match.groups())  # ('an', 'age', '23')
    print(len(match.groups()))  # 3
