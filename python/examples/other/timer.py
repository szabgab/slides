import random
import time

# https://docs.python.org/3/library/time.html#time.struct_time

print(time.time())     # time since the epoch in seconds
print(time.asctime())  # current local time in human-readable format
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # create your own human-readable format

print(time.gmtime(0))  # epoch
print(time.asctime(time.gmtime(0)))  # epoch in human-readable format

print(time.localtime()) # local time now
print(time.gmtime()) # time in London



print(time.process_time())
print(time.process_time_ns())

s = time.perf_counter()
ps = time.process_time()
print(time.monotonic())
time.sleep(0.1)
print(time.monotonic())
e = time.perf_counter()
for _ in range(100000):
    random.random()
pe = time.process_time()
print(s)
print(e)
print(e-s)
print(pe-ps)

# print(time.get_clock_info('monotonic'))
