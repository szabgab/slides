import os
from my_tempdir import my_tempdir

with my_tempdir() as tmp_dir:
    print(f"In return context with {tmp_dir}")
    with open(tmp_dir + '/data.txt', 'w') as fh:
        fh.write("hello")
    print(os.listdir(tmp_dir))
    raise Exception('trouble')

print('')
print(tmp_dir)
print(os.path.exists(tmp_dir))
