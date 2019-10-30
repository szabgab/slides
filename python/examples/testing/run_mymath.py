import mymath
import sys

if len(sys.argv) != 4:
    exit("Usage: {} [add|div] INT INT".format(sys.argv[0]))

if sys.argv[1] == 'add':
    print(mymath.add(int(sys.argv[2]), int(sys.argv[3])))
if sys.argv[1] == 'div':
    print(mymath.div(int(sys.argv[2]), int(sys.argv[3])))

