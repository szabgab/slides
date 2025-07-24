import sys
file = sys.argv[0]

with open(file) as fh:
    print(len(fh))

