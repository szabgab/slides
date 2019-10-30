import threading, sys
print = lambda x: sys.stdout.write("{}\n".format(x))

class AsyncCount(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print('{} - start'.format(thread.name))
        for c in range(10):
            print('{} - count {}'.format(thread.name, c))
        print('{} - end'.format(thread.name))
        return

a = AsyncCount()
b = AsyncCount()
a.start()
b.start()

print('main - running {} threads including the main thread'
    .format(threading.active_count()))

a.join()
b.join()
print("main - thread is done")
