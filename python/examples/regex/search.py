import re

match = re.search(r'lac', 'The black cat climed')
if match:
    print("Matching")       # Matching
    print(match.group(0))   # lac

match = re.search(r'dog', 'The black cat climed')
if match:
    print("Matching")
else:
    print("Did NOT match")
    print(match)     # None
