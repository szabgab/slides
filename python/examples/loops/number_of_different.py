import sys

if len(sys.argv) != 2:
    exit("Need a string to count")

text = sys.argv[1]

unique = ''
for cr in text:
    if cr not in unique:
        unique += cr

print(len(unique))
