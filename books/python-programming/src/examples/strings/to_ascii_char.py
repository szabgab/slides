import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} CHARACTER")

print( ord( sys.argv[1]) )
