import subprocess
import sys
import time


proc = subprocess.Popen([sys.executable, 'slow.py'],
   stdout = subprocess.PIPE,
   stderr = subprocess.PIPE,
)

#out, err = proc.communicate()  # this is when the code starts executing
#print(out)
#print(err)

timeout = 6
while True:
   poll = proc.poll()
   print(poll)
   time.sleep(0.5)
   timeout -= 0.5
   if timeout <= 0:
       break
   if poll is not None:
       break

print("Final: {}".format(poll))
if poll is None:
   pass
else:
   out, err = proc.communicate()
   print(out)
   print(err)
