import multitasking
import time
import random

@multitasking.task
def first(count):
    sleep = random.randint(1,10)/2
    if count == 10:
        sleep = 10
    print("Start First {} (sleeping for {}s)".format(count, sleep))
    time.sleep(sleep)
    print("finish First {} (after for {}s)".format(count, sleep))

@multitasking.task
def second(count):
    sleep = random.randint(1,10)/2
    print("Start Second {} (sleeping for {}s)".format(count, sleep))
    time.sleep(sleep)
    print("finish Second {} (after for {}s)".format(count, sleep))

if __name__ == "__main__":
    for i in range(0, 10):
        first(i+1)
    multitasking.wait_for_tasks()
    print('first done')

    for i in range(0, 10):
        second(i+1)

    multitasking.wait_for_tasks()
    print('second done')
