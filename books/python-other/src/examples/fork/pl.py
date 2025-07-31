from multiprocessing import Pool
import time
import os
import random

def f(x):
    #print(os.getpid())
    #time.sleep(1)
    for _ in range(100000000):
        random.random()
    return x*x

if __name__ == '__main__':
    numbers = list(range(30))

    start = time.time()
    with Pool(5) as p:
        print(p.map(f, numbers))
    end = time.time()
    print(f"Elapsed time: {end-start}")

    start = time.time()
    print(list(map(f, numbers)))
    end = time.time()
    print(f"Elapsed time: {end-start}")

    start = time.time()
    with Pool(30) as p:
        print(p.map(f, numbers))
    end = time.time()
    print(f"Elapsed time: {end-start}")



