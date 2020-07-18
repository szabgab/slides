import sys

def process_file(filename):
    with open(filename, 'r') as fh:

        for line in fh:
            line = line.rstrip("\n")
            if len(line) > 0:
                if line[0] == '#':
                    return
# some comment

            if len(line) > 1:
                if line[0:2] == '//':
                    return

            print(line)


process_file(sys.argv[0])
