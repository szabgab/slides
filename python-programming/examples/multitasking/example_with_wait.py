import multitasking
import time
import random

multitasking.set_max_threads(2)

@multitasking.task
def work(ix, sec):
    print(f"Start {ix} sleeping for {sec}s")
    time.sleep(sec)
    print(f"Finish {ix}")

if __name__ == "__main__":
    tasks = (6, 0.7, 0.8, 0.3, 0.4, 3, 0.1)
    for ix, sec in enumerate(tasks):
        work(ix+1, sec)
    multitasking.wait_for_tasks()

    print("do some work after all the jobs are done")
