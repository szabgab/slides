import re

text = 'The black cat climed'
match = re.search(r'lac', text)
if match:
    print("Matching")       # Matching
    print(match.group(0))   # lac

match = re.search(r'dog', text)
if match:
    print("Matching")
else:
    print("Did NOT match")
    print(match)     # None
