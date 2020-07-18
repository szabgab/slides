import re

line = 'There is a phone number 12345 in this row and an age: 23'

match = re.search(r'age: \d+', line)
if match:
  print(match.group(0))  # age: 23


match = re.search(r'age: (\d+)', line)
if match:
    print(match.group(0))  # age: 23
    print(match.group(1))  # 23      the first group of parentheses

    print(match.groups())  # ('23',)
    print(len(match.groups()))  # 1

