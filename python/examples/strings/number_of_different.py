import sys

s = sys.argv[1]

unique = ''
for c in s:
    if c not in unique:
        unique += c

print(len(unique))
