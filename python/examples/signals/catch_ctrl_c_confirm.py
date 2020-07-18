import signal
import time

def handler(signum, frame):
    answer = input('We are almost done. Do you really want to exit? [yes]:')
    if answer == 'yes':
        print('bye')
        exit()
    print("Then let's keep running")

signal.signal(signal.SIGINT, handler)

for _ in range(10):
    time.sleep(5)

