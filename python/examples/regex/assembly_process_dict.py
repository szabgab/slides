import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    code = fh.read()


mapping = {
    'R1' : 'R2',
    'R2' : 'R3',
    'R3' : 'R1',
}

code = re.sub(r'\b(R[123])\b', lambda match: mapping[match.group(1)], code)
print(code)

# The same but now with a named function for clarity
def replace(match):
    original = match.group(1)
    return mapping[original]

code = re.sub(r'\b(R[123])\b', replace, code)
print(code)
