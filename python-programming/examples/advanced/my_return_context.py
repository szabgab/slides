from contextlib import contextmanager

import time
import random
import os
import shutil


@contextmanager
def my_return_context():
   print("start return")
   tmpdir = '/tmp/' + str(time.time()) + str(random.random())
   os.mkdir(tmpdir)
   yield tmpdir
   shutil.rmtree(tmpdir)
   print("end return")

with my_return_context() as tmp_dir:
   print(f"In return context with {tmp_dir}")
   with open(tmp_dir + '/data.txt', 'w') as fh:
       fh.write("hello")
   print(os.listdir(tmp_dir))

print('')
print(tmp_dir)
print(os.path.exists(tmp_dir))
