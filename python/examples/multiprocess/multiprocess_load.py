import random
import multiprocessing
import time
import sys
# Works only in Python 3

def calc(n):
    count = 0
    total = 0
    while count < 40000000 / n:
        rnd = random.random()
        total += rnd
        count += 1
    return {'count': count, 'total': total}

def main():
    if len(sys.argv) != 2:
        exit("Usage: {} POOL_SIZE")

    start = time.time()
    size = int(sys.argv[1])
    with multiprocessing.Pool(size) as pool:
        results = pool.map(calc, [size] *  size)
        print("Results: {}".format(results))
        totals = map(lambda r: r['total'], results)
        print("Total: {}".format(sum(totals)))
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
