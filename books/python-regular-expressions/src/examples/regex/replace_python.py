import sys
import re

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} INFILE")

infile = sys.argv[1]

with open(infile, 'r') as inf:
    for row in inf:
        row = row.rstrip("\n")
        row = re.sub(r'(?<!Monty )Python', 'Java', row)
        row = re.sub(r'(?<!Monty )python', 'java', row)
        print(row)

