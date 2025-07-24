import sys

file = sys.argv[0]

with open(file) as fh:
    for row in fh:
        print(row, end="")

