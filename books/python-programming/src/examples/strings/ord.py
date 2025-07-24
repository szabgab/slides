import sys

filename = sys.argv[1]

with open(filename) as fh:
   content = fh.read()

for c in content:
   print(ord(c))

