import sys

if len(sys.argv) < 2:
    exit("Need name of file.")

counter = [0] * 10
filename = sys.argv[1]
with open(filename) as fh:
    for line in fh:
        for c in line.rstrip("\n"):
            if c == ' ':
                continue

            c = int(c)
            counter[c] += 1

for i in range(10):
    print("{} {}".format(i, counter[i]))
