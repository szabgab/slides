import time
import sys
import os

if len(sys.argv) != 3:
    exit(f"{sys.argv[0]} SECONDS EXIT_CODE")

print(f"process ID: {os.getpid()}  parent ID: {os.getppid()}")

seconds = int(sys.argv[1])
exit_code = int(sys.argv[2])

for sec in range(seconds):
   print("OUT {}".format(sec), flush=True)
   print("ERR {}".format(sec), file=sys.stderr)
   time.sleep(1)

exit(exit_code)
