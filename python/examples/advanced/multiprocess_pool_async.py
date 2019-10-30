#!/usr/bin/env python3
from multiprocessing import Pool
import os


def f(x):
    print("Input {} in process {}".format(x, os.getpid()))
    return x*x

def prt(z):
    print(z)

if __name__ == '__main__':
    with Pool(5) as p:
        results = p.imap(f, range(11)) # <multiprocessing.pool.IMapIterator object
        print(results)
        print('--')
        for r in results:
            print(r)

        #results = p.map_async(f, range(11))  # <multiprocessing.pool.MapResult object>, not iterable

        #results = []
        #p.map_async(f, range(11))  # <multiprocessing.pool.MapResult object>, not iterable
        #print(results)
        #for r in results:
        #    print(r)


