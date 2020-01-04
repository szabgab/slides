#!/usr/bin/env python

from Queue import Queue 
from threading import Thread

def source():
    """Returning the list of tasks"""
    return range(1, 10)

def do_work(item):
    print "Working on item " + str(item) + "\n",
# print "Working on item ", str(item)
# would show the output intermingled as the separate items of the print statement
# (even the trailing newline) might be printed only after context switch


def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

def main():
    for i in range(num_worker_threads):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    for item in source():
        q.put(item)

    q.join()       # block until all tasks are done

num_worker_threads = 3
q = Queue()
main()
