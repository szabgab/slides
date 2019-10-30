import random
import multiprocessing
import time
import sys
# Works only in Python 3

c = 0

def f(n):
    global c
    i = 0
    while i < 40000000 / n:
        x = random.random()
        y = random.random()
        z = x + y
        i += 1
    return  z

if __name__ == '__main__':
    s = time.time()
    n = int(sys.argv[1])
    with multiprocessing.Pool(n) as p:
        dicts = p.map(f, [n]*n)
        print(dicts)
    print(time.time() - s)

