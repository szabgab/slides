import re

line = 'There is a phone number 12345 in this row and another 42 number'
match = re.search(r'(\w+) (\d+)', line)
if match:
    print(match.group(1))   # number
    print(match.group(2))   # 12345

matches = re.findall(r'(\w+) (\d+)', line)
print(matches)  # [('number', '12345'), ('another', '42')]

