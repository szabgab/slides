import os
import sys

if len(sys.argv) != 2:
    exit("Usage: {} directory".format(sys.argv[0]))

path = sys.argv[1]
things = os.listdir(path)

for name in things:
    print(name)
    print(os.path.join(path, name))
