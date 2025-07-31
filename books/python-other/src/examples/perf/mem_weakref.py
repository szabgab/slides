import sys
from weakmymem import alloc

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} N")

count = int(sys.argv[1])

for _ in range(count):
    alloc()
input("End the script")

