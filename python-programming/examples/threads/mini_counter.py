import threading
import sys

class ThreadedCount(threading.Thread):
    def run(self):
        for c in range(10):
            print(c)
        return

a = ThreadedCount()
b = ThreadedCount()
c = ThreadedCount()

a.start()
b.start()
c.start()
print('main - Running {} threads'.format(threading.active_count()))

a.join()
b.join()
c.join()
print("main - thread is done")
