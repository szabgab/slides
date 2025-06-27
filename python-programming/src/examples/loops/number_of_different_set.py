import sys

if len(sys.argv) != 2:
    exit("Need a string to count")

text = sys.argv[1]

set_of_chars = set(text)

print(len(set_of_chars))

