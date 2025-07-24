import sys
import random
import time

def add_random(result_filename, count, wait, exception=''):
    total = 0
    for _ in range(int(count)):
        total += random.random()

    time.sleep(float(wait))
    if exception:
        raise Exception(exception)

    with open(result_filename, 'w') as fh:
        fh.write(str(total))


if __name__ == '__main__':
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        exit(f"Usage: {sys.argv[0]} RESULT_FILENAME COUNT WAIT [EXCEPTION]")
    add_random(*sys.argv[1:])
