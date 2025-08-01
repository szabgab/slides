import threading
import sys
import time

cnt = 0
num = 30
limit = 100000

locker = threading.Lock()

class ThreadedCount(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.counter = 0
    def run(self):
        global cnt
        while self.counter < limit:
            self.counter += 1
            locker.acquire()
            cnt += 1
            locker.release()
        return

start = time.time()
threads = [ ThreadedCount() for n in range(num) ]
[ t.start() for t in threads ]
[ t.join() for t in threads ]
end = time.time()

print("Expected: {}".format(num * limit))
print("Received: {}".format(cnt))
print("Elapsed: {}".format(end-start))

# Expected: 3000000
# Received: 3000000
# Elapsed: 12.333643198013306
