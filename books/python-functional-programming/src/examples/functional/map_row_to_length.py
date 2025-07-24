import sys
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")
filename = sys.argv[1]

with open(filename) as fh:
    length = map(len, fh)
    print(length)
    for ln in length:
        print(ln)
        # if ln > 10:
        #     break
