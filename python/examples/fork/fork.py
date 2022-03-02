import os
import time

name = "common"

def child():
    time.sleep(1)
    print(f"In Child ({name}).")
    print(f"In Child PID: {os.getpid()} PPID: {os.getppid()}")

    time.sleep(5)
    exit(3)

def parent(child_pid):
    time.sleep(1)
    print(f"In Parent ({name}) The child is: {child_pid}")
    print(f"In Parent PID: {os.getpid()} PPID: {os.getppid()}")
    r = os.wait()
    print(r)

print(f'{os.getpid()} - start running')
pid = os.fork()
print(f'my pid: {os.getpid()} pid received from fork: {pid}')
if pid == 0:
    child()
else:
    parent(pid)

