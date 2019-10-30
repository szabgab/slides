import threading, sys
print = lambda x: sys.stdout.write("{}\n".format(x))

class AsyncCount(threading.Thread):
    def __init__(self, name, start, stop):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = start
        self.limit = stop
        print('__init__  of {} in {}'
            .format(self.name, threading.current_thread()))
    def run(self):
        print('start run of {} in {}'
            .format(self.name, threading.current_thread()))
        while self.counter < self.limit:
            print('count {} of {}'.format(self.name, self.counter))
            self.counter += 1
        print('end run   of {} in {}'
            .format(self.name, threading.current_thread()))
        return

foo = AsyncCount("Foo", 1, 11)
bar = AsyncCount("Bar", 1, 11)
foo.start()
bar.start()
print('main - running {} threads'.format(threading.active_count()))
foo.join()
bar.join()
print("main - thread is done")
