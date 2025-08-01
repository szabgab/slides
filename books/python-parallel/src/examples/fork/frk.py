import os
import time

print(f"before: {os.getpid()}")

pid = os.fork()
if pid == 0:
    print(f"child {os.getpid()}")
    time.sleep(20)
    exit()
else:
    print(f"parent {os.getpid()} after creating {pid}")

