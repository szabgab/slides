import multiprocessing as mp
import os
import sys
import fcntl

filename = "counter.txt"

#def increment():
#    # print("increment")
#    cnt = 0
#    if os.path.exists(filename):
#        with open(filename) as fh:
#            cnt = int(fh.read())
#    cnt += 1
#    with open(filename, 'w') as fh:
#        fh.write(str(cnt))

# def increment():
#     # print("increment")
#     cnt = 0
#     if not os.path.exists(filename):
#         with open(filename, 'w') as fh:
#             fh.write("0")
#
#     with open(filename, 'r+') as fh:
#         cnt = int(fh.read())
#         fh.seek(os.SEEK_SET, 0)
#         cnt += 1
#         fh.write(str(cnt))

def increment():
    # print("increment")
    cnt = 0
    if not os.path.exists(filename):
        with open(filename, 'w') as fh:
            fcntl.flock(fh, fcntl.LOCK_EX)
            fh.write("0")

    with open(filename, 'r+') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        cnt = int(fh.read())
        fh.seek(0, 0)
        fh.truncate(0)
        cnt += 1
        fh.write(str(cnt))


def count(n):
    for _ in range(n):
        increment()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} PARALLEL")
    size = int(sys.argv[1])

    if os.path.exists(filename):
        os.unlink(filename)

    with mp.Pool(size) as pool:
        pool.map(count, [10, 10])

    with open(filename) as fh:
        print(fh.read())


