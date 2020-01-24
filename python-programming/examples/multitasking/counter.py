import multitasking
import time


multitasking.set_max_threads(10)
counter = 0


@multitasking.task
def count(n):
    global counter
    for _ in range(n):
        counter += 1


if __name__ == "__main__":
    start = time.time()
    k = 10
    n = 1000000
    for _ in range(k):
        count(n)
    multitasking.wait_for_tasks()
    end = time.time()
    expected = k * n
    print(f'done actual: {counter} expected: {expected}. Missing: {expected-counter}')
    print(f'Elapsed time {end-start}')
