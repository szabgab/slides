import sys
from mymem import alloc
import gc

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} N")

count = int(sys.argv[1])

for _ in range(count):
    alloc()
input("Run gc")

gc.collect()
input("End the script")

