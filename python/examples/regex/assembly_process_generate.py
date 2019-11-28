import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    code = fh.read()


# or without any assumption and in one substitution:
mapping = {
    'R1'  : 'R2',
    'R2'  : 'R3',
    'R3'  : 'R1',
    'R12' : 'R21',
    'R21' : 'R12',
}

regex = r'\b(' + '|'.join(mapping.keys()) + r')\b'

code = re.sub(regex, lambda match: mapping[match.group(1)], code)

print(code)
