import os, time, random

print('{} - start running'.format(os.getpid()))

pid = os.fork()
if not pid:
    #random.seed()
    print('{} - in child'.format(os.getpid()))
    print(random.random())
    time.sleep(1)
    exit(3)

print('{} - in parent (child pid is {})'.format(os.getpid(), pid))
print(random.random())

done = os.wait()
print('{} - Child exited {}'.format(os.getpid(), done))

