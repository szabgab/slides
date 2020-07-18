# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
import time, sys

for i in range(10):
    sys.stdout.write('\r' +  '=' * i)
    sys.stdout.flush()
    time.sleep(1)


