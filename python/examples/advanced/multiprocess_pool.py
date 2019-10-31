from multiprocessing import Pool
import os
import sys

def f(x):
    print("Input {} in process {}".format(x, os.getpid()))
    #print(x)
    return x*x

def main():
    if len(sys.argv) != 3:
        exit("Usage: {} NUMBERS POOL_SIZE")
    numbers = int(sys.argv[1])
    size    = int(sys.argv[2])

    with Pool(size) as p:
        results = p.map(f, range(numbers))
    print(results)

main()

