import os
import sys

if len(sys.argv) != 2:
    exit("Usage: {} directory".format(sys.argv[0]))

path = sys.argv[1]
files = os.listdir(path)
for name in files:
    print(name)
    print(os.path.join(path, name))

