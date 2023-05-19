import multiprocessing
import os
import sys

def f(x):
    print(f"Input {x} in process {os.getpid()}")
    return x*x

def main():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} NUMBERS POOL_SIZE")
    numbers = int(sys.argv[1])
    size    = int(sys.argv[2])

    with multiprocessing.Pool(size) as p:
        results = p.map(f, range(numbers))
    print(results)

if __name__ == '__main__':
    main()
