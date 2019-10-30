filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
    for line in fh:
        print(line)            # duplicate newlines

# close is called when we leave the 'with'
