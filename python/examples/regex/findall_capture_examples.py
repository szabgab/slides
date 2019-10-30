import re

line = 'There is a phone number 83795 in this row and another 42 number'
print(line)

search = re.search(r'(\d)(\d)', line)
if search:
  print(search.group(1))   # 8
  print(search.group(2))   # 3

matches = re.findall(r'(\d)(\d)', line)
if matches:
  print(matches)  # [('8', '3'), ('7', '9'), ('4', '2')]

matches = re.findall(r'(\d)\D*', line)
if matches:
  print(matches)  # [('8', '3', '7', '9', '5', '4', '2')]

matches = re.findall(r'(\d)\D*(\d?)', line)
print(matches)  # [('8', '3'), ('7', '9'), ('5', '4'), ('2', '')]

matches = re.findall(r'(\d).*?(\d)', line)
print(matches) # [('8', '3'), ('7', '9'), ('5', '4')]

matches = re.findall(r'(\d+)\D+(\d+)', line)
print(matches) # [('83795', '42')]

matches = re.findall(r'(\d+).*?(\d+)', line)
print(matches) # [('83795', '42')]

matches = re.findall(r'\d', line)
print(matches) # ['8', '3', '7', '9', '5', '4', '2']
