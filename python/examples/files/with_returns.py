import sys

def process_file(filename):
    with open(filename, 'r') as fh:

        for line in fh:
            line = line.rstrip("\n")
            if len(line) > 0 and line[0] == '#':
                return

            if len(line) > 1 and line[0:2] == '//':
                return

            # process the line
            print(line)


process_file(sys.argv[0])
