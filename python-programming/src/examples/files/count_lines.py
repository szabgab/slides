import sys
if len(sys.argv) != 2:
    exit(f"Run {sys.argv[0]} FILENAME")

filename = sys.argv[1]

with open(filename, 'r') as fh:
    count = 0
    for row in fh:
        if count == 2:
            break
        count += 1
print(row)
