import sys
import re

# data: field_value_pairs.txt
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

with open(filename) as fh:
    for line in fh:
        line = line.rstrip("\n")
        field, value = re.split(r'\s*=\s*', line)
        print(f"{value}={field}")
