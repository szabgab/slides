import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename) as fh:
    code = fh.read()

code = re.sub(r'R1', 'R4', code)
code = re.sub(r'R3', 'R1', code)
code = re.sub(r'R2', 'R3', code)
code = re.sub(r'R4', 'R2', code)

print(code)
