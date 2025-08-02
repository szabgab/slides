import os
import time

with open("first.txt", "w") as fh:
    fh.flush()
    pass
print(f"time: {time.time()}")
#time.sleep(0.01)
with open("second.txt", "w") as fh:
    pass
first = os.path.getmtime("first.txt")
second = os.path.getmtime("second.txt")
print(first)
print(second)
print("same" if first == second else "diff")

