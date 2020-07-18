import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    code = fh.read()


# or without any assumption and in one substitution:
mapping = {
    'R1' : 'R2',
    'R2' : 'R3',
    'R3' : 'R1',
}

code = re.sub(r'\b(R[123])\b', lambda match: mapping[match.group(1)], code)

print(code)
