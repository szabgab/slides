import threading
import sys

class ThreadedCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('{} - start'.format(thread.name))
        for c in range(10):
            print('{} - count {}'.format(thread.name, c))
        print('{} - end'.format(thread.name))
        return

a = ThreadedCount()
b = ThreadedCount()
c = ThreadedCount()
a.start()
b.start()
c.start()

print('main - running {} threads'.format(threading.active_count()))

a.join()
b.join()
c.join()
print("main - thread is done")
