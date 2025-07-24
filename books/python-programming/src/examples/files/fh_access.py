import sys
if len(sys.argv) != 2:
    exit(f"Run {sys.argv[0]} FILENAME")

filename = sys.argv[1]

# We can iterate over the lines
#with open(filename, 'r') as fh:
#    for line in fh:
#        print(line)

# We cannot access an element
with open(filename, 'r') as fh:
    print(fh[2])
