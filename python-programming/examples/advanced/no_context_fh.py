import sys
import re

def do_something(filename):
    fh = open(filename)

    while True:
        line = fh.readline()
        if line is None:
            break
        line = line.rstrip("\n")

        if re.search(r'\A\s*\Z', line):
            return
        print(line)

    fh.close()

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]
    do_something(filename)

main()
