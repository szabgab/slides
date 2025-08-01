from multiprocessing import Process
import os
import time

start = time.time()

def f(param, sec):
    print(f"f{start} {time.time()} f({param}) pid:{os.getpid()} parent: {os.getppid()} enter")
    time.sleep(sec)
    print(f"f{start} {time.time()} f({param}) pid:{os.getpid()} parent: {os.getppid()} exit")

def g(param):
    print(f"f{start} {time.time()} g({param}) pid:{os.getpid()} parent: {os.getppid()} enter")
    pr = Process(target = f, args=['procs', 3])
    print("before start")
    pr.start()
    #pr.join()
    f("world", 0)
    print(f"f{start} {time.time()} g({param}) pid:{os.getpid()} parent: {os.getppid()} exit")


g("hello")


