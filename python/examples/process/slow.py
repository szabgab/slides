import time
import sys

for i in range(3):
   print("OUT {}".format(i))
   print("ERR {}".format(i), file=sys.stderr)
   time.sleep(1)

