import time

start = time.time()
print("hello " + str(start))

time.sleep(3.5)

end = time.time()
print("world " + str(end))
print("Elapsed time:" + str(end-start))
