import re

filename = "mixed.txt"

with open(filename) as fh:
    lines = fh.readlines()
for line in lines:
    if re.search('\N{IN HEBREW}', line):
        print(line)
