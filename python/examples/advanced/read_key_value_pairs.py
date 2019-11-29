import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]}")

filename = sys.argv[1]

with open(filename) as fh:
    pairs = dict(map(lambda x: x.split('='), map(lambda s: s.rstrip("\n"), fh.readlines())))

print(pairs)
