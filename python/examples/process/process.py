import time
import sys

if len(sys.argv) != 3:
    exit(f"{sys.argv[0]} SECONDS EXIT_CODE")

seconds = int(sys.argv[1])
exit_code = int(sys.argv[2])

for sec in range(seconds):
   print("OUT {}".format(sec))
   print("ERR {}".format(sec), file=sys.stderr)
   time.sleep(1)

exit(exit_code)
