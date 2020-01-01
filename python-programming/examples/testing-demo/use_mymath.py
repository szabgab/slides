import mymath
import sys

if len(sys.argv) != 3:
    exit(f"Usage {sys.argv[0]} NUMBER NUMBER")

a = int(sys.argv[1])
b = int(sys.argv[2])

print(mymath.add(a, b) )
