import time
import sys
import os

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} SECONDS")

print(f"{int(time.time())} - start will take {sys.argv[1]} seconds (pid: {os.getpid()})", flush=True)
time.sleep(int(sys.argv[1]))
print(f"{int(time.time())} - started", flush=True)

while True:
    time.sleep(1)
    print(f"{int(time.time())} - running", flush=True)
