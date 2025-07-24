import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} NUMBER")

print( chr( int(sys.argv[1]) ) )
