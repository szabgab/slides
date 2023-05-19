import multiprocessing
import os


def f(x):
    print(f"Input {x} in process {os.getpid()}")
    return x*x

def prt(z):
    print(z)

def main():
    with multiprocessing.Pool(5) as p:
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


if __name__ == '__main__':
    main()
