import sys
if len(sys.argv) != 2:
    exit(f"Run {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename, 'r') as fh:
    rows = fh.readlines()
print(rows[2])
