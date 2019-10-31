import random
import multiprocessing
import time
import sys
# Works only in Python 3

def calc(n):
    i = 0
    while i < 40000000 / n:
        x = random.random()
        y = random.random()
        z = x + y
        i += 1
    return  z

def main():
    if len(sys.argv) != 2:
        exit("Usage: {} POOL_SIZE")

    start = time.time()
    size = int(sys.argv[1])
    with multiprocessing.Pool(size) as pool:
        dicts = pool.map(calc, [size] *  size)
        print(dicts)
    end = time.time()
    print(end - start)

main()

