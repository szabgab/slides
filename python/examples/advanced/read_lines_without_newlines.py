import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]}")

filename = sys.argv[1]

with open(filename) as fh:
    rows = map(lambda s: s.rstrip("\n"), fh.readlines())

for row in rows:
    print(row)
