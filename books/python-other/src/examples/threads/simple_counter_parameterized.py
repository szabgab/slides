import threading
import sys

num_threads, count_till = 3, 5

class ThreadedCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print(f'{thread.name} - start')
        for cnt in range(count_till):
            print(f'{thread.name} - count {cnt}')
        print(f'{thread.name} - end')
        return

threads = []
for ix in range(num_threads):
    threads.append(ThreadedCount())

for th in threads:
    th.start()

print('main - running {} threads'.format(threading.active_count()))

for th in threads:
    th.join()
print("main - thread is done")
