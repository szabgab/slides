import threading, Queue

class AsyncCount(threading.Thread):
    def __init__(self, name, start, stop):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = start
        self.limit = stop
    def run(self):
        while self.counter < self.limit:
            self.counter += 1
            print(self.name, self.counter)

        print(self.name , "finished")
        return

q = Queue()
foo = AsyncCount("Foo", 1, 10)
bar = AsyncCount("Bar", 1, 10)
foo.start()
bar.start()
print("main - running")

foo.join()
bar.join()
print("main - thread is done")
