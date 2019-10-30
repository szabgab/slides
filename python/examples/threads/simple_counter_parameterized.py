import threading, sys
print = lambda x: sys.stdout.write("{}\n".format(x))

num_threads, count_till = 3, 5

class AsyncCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('{} - start'.format(thread.name))
        for c in range(count_till):
            print('{} - count {}'.format(thread.name, c))
        print('{} - end'.format(thread.name))
        return

threads = []
for i in range(num_threads):
    threads.append(AsyncCount())
for t in threads:
    t.start()

print('main - running {} threads including the main thread'
    .format(threading.active_count()))

for t in threads:
    t.join()
print("main - thread is done")
