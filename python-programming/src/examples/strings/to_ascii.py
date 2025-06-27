import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} STRING")

for cr in sys.argv[1]:
    print( ord( cr ) )
