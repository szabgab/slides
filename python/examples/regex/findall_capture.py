import re

line = 'There is a phone number 12345 in this row and another 42 number'
match = re.search(r'\w+ \d+', line)
if match:
    print(match.group(0))   # number 12345

match = re.search(r'\w+ (\d+)', line)
if match:
    print(match.group(0))   # number 12345
    print(match.group(1))   # 12345

matches = re.findall(r'\w+ \d+', line)
print(matches)  # ['number 12345', 'another 42']

matches = re.findall(r'\w+ (\d+)', line)
print(matches)  # ['12345', '42']

