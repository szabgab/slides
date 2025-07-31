import multiprocessing as mp
import os

def func():
    print("proc pid: {} parent pid: {}".format(os.getpid(), os.getppid()))

def main():
    print("main pid: {} before".format(os.getpid()))
    proc = mp.Process(target=func)
    proc.start()
    proc.join()
    print("main pid: {} after".format(os.getpid()))


if __name__ == '__main__':
    main()

