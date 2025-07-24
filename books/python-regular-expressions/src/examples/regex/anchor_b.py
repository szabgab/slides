import re

text = 'x a xyb x-c qwer_  ut!@y'

print(re.findall(r'.\b.', text))

print(re.findall(r'\b.', 'a b '))

print(re.findall(r'.\b', 'a b '))

