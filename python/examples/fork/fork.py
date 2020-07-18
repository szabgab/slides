import os
import time

name = "common"

def child():
    print("In Child of {}".format(name))
    print("In Child PID: {} PPID: {}".format(os.getpid(), os.getppid()))

    time.sleep(5)
    exit(3)

def parent(child_pid):
    print("In Parent ({}) The child is: {}".format(name, child_pid))
    print("In Parent PID: {} PPID: {}".format(os.getpid(), os.getppid()))
    r = os.wait()
    print(r)

pid = os.fork()
print(pid)
if pid == 0:
    child()
else:
    parent(pid)

