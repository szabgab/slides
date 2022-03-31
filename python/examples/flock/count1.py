import sys
import os
import time

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME count")
filename, count = sys.argv[1:]
print(f"start {os.getpid()}")
time.sleep(1)

for _ in range(int(count)):
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as fh:
                fh.write("0\n")
        with open(filename, 'r') as fh:
            number = int(fh.readline())
            number += 1
            with open(filename, 'w') as fh:
            #fh.seek(0,0)
                fh.write(f"{number}\n")
    except Exception:
        pass
print(f"done {os.getpid()}")

