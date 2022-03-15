import sys

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]
    with open(filename) as fh:
        print("Working on the file", filename)

main()
