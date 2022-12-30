import re

text = """  First row
Second row
  Third row
"""

print(text)
print('-----')
print(re.sub(r'^\s+', '', text))
print('-----')
print(re.sub(r'\A\s+', '', text, flags=re.MULTILINE))
print('-----')
print(re.sub(r'^\s+', '', text, flags=re.MULTILINE))
