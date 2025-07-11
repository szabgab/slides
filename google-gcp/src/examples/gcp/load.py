import random
import time
import sys

if len(sys.argv) != 2:
    exit('Pass the load')

load = int(sys.argv[1])

while True:
    z = 0
    for _ in range(load):
        x = random.random()
        z += z
    time.sleep(0.000001)
