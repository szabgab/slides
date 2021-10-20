import sys
import codecs

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]
with open(filename, 'r') as fh:
    original = fh.read()

encoded = codecs.encode(original, encoding='rot_13')
#print(encoded)

with open(filename, 'w') as fh:
    fh.write(encoded)
