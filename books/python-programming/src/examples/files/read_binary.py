import sys
if len(sys.argv) != 2:
    exit("Need name of file")

filename = sys.argv[1]

try:
    with open(filename, 'rb') as fh:
        while True:
            binary_str = fh.read(1000)
            print(len(binary_str))
            if len(binary_str) == 0:
                break
            # do something with the content of the binary_str
except Exception:
    pass

