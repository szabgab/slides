import sys
import time

cnt = 0
num = 30
limit = 100000

class Count():
    def __init__(self):
        self.counter = 0
    def run(self):
        global cnt
        while self.counter < limit:
            self.counter += 1
            cnt += 1
        return

start = time.time()
for _ in range(num):
    c = Count()
    c.run()
end = time.time()

print("Expected: {}".format(num * limit))
print("Received: {}".format(cnt))
print("Elapsed: {}".format(end-start))

# Expected: 3000000
# Received: 3000000
# Elapsed: 0.4130408763885498

