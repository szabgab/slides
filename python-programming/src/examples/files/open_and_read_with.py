filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:   # open(filename) would be enough
    for line in fh:
        print(line)               # duplicate newlines

# close is called when we leave the 'with' context
