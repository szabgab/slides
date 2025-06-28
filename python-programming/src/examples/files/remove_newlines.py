import sys
filename = sys.argv[0]
with open(filename) as fh:
    lines = []
    for line in fh:
        lines.append(line.rstrip("\n"))
    print(lines)
