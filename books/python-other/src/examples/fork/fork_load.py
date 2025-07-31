import os
import random
import sys

if len(sys.argv) != 2:
    exit("Usage: {} N".format(sys.argv[0]))
n = int(sys.argv[1])
for p in range(0, n):
    pid = os.fork()
    if not pid:
        print('In Child')
        i = 0
        while i < 40000000/n:
            x = random.random()
            y = random.random()
            z = x+y
            i += 1
        exit(3)
    print('In Parent of', pid)

for p in range(0, n):
    r = os.wait()
    print(r)

