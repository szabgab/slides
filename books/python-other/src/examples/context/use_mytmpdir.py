from mytmpdir import tmpdir
import os

with tmpdir() as temp_dir:
    print(temp_dir)
    with open( os.path.join(temp_dir, 'some.txt'), 'w') as fh:
        fh.write("hello")
    print(os.path.exists(temp_dir))
    print(os.listdir(temp_dir))

print(os.path.exists(temp_dir))
