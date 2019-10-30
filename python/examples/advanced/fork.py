import os, time

print('{} - start running'.format(os.getpid()))

pid = os.fork()
if not pid:
    print('{} - in child'.format(os.getpid()))
    time.sleep(1)
    exit(3)

print('{} - in parent (child pid is {})'.format(os.getpid(), pid))

done = os.wait()
print('{} - Child exited {}'.format(os.getpid(), done))

