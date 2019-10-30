import sys

print("hello")
sys.stderr.write("world\n")

print('spam', file=sys.stderr)

