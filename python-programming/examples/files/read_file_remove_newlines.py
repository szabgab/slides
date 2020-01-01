filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
    for line in fh:
        line = line.rstrip("\n")
        print(line)
