import threading, random, sys
print = lambda x: sys.stdout.write("{}\n".format(x))

thread_count = 5

counter = 0
queue = map(lambda x: ('main', random.randrange(5)), range(20))
print(queue)
