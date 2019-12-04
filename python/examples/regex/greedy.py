import re

match = re.search(r'xa*', 'xaaab')
print(match.group(0))

match = re.search(r'xa*', 'xabxaab')
print(match.group(0))

match = re.search(r'a*',  'xabxaab')
print(match.group(0))

