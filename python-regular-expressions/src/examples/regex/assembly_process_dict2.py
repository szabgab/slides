import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    code = fh.read()

mapping = {
    'R1'  : 'R2',
    'R2'  : 'R3',
    'R3'  : 'R1',
    'R12' : 'R21',
    'R21' : 'R12',
}

code = re.sub(r'\b(R1|R2|R3|R12)\b', lambda match: mapping[match.group(1)], code)

print(code)

