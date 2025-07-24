import sys
if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} [os|math]")
print(dir())
print()

cls = __import__(sys.argv[1])
print(dir())
print()

print(dir(cls))
