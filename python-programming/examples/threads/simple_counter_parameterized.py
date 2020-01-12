import threading
import sys

num_threads, count_till = 3, 5

class ThreadedCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('{} - start'.format(thread.name))
        for c in range(count_till):
            print('{} - count {}'.format(thread.name, c))
        print('{} - end'.format(thread.name))
        return

threads = []
for i in range(num_threads):
    threads.append(ThreadedCount())
for t in threads:
    t.start()

print('main - running {} threads'.format(threading.active_count()))

for t in threads:
    t.join()
print("main - thread is done")
