from multiprocessing import Process
import time
import os

# This shows that there is copy on write and the memory starts duplicating only when we change the variable that was inherited from the parent.

limit = 300000000
x = ["y"] * limit
print("wait")


def wait(cr):
    print(f"called wait in {os.getpid()}")
    for i in range(limit):
        x[i] = cr;
    print(f"wating in {os.getpid()}")
    time.sleep(100)

p1 = Process(target = wait, args=['a'])
p1.start()
wait('y')
p1.join()

