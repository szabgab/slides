import re

line = 'There is a phone number 12345 in this row and an age: 23'

match = re.search(r'((\w+): (\d+))', line)
if match:
    print(match.group(0))  # age: 23
    print(match.group(1))  # age: 23
    print(match.group(2))  # age 
    print(match.group(3))  # 23
    
    print(match.groups())  # ('age: 23', 'age', '23')
    print(len(match.groups()))  # 3


