filename = 'examples/files/numbers.txt'

fh = open(filename, 'r')
for line in fh:
    print(line)
fh.close()
