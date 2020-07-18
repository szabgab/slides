import re

line = "abc123def"

print(re.sub(r'\d+', ' ', line)) # "abc def"
print(line)                      # "abc123def"

print(re.sub(r'x', ' y', line))  # "abc123def"
print(line)                      # "abc123def"

print(re.sub(r'([a-z]+)(\d+)([a-z]+)', r'\3\2\1', line))   #  "def123abc"
print(re.sub(r'''
([a-z]+)     # letters
(\d+)        # digits
([a-z]+)     # more letters
''', r'\3\2\1', line, flags=re.VERBOSE))   #  "def123abc"

print(re.sub(r'...', 'x', line))             # "xxx"
print(re.sub(r'...', 'x', line, count=1))    # "x123def"

print(re.sub(r'(.)(.)', r'\2\1', line))            # "ba1c32edf"
print(re.sub(r'(.)(.)', r'\2\1', line, count=2))   # "ba1c23def"
