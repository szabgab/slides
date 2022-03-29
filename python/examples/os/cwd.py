import sys
import os

to_dir = '..'
# to_dir = '/path/to/some/dir'
if len(sys.argv) == 2:
    to_dir = sys.argv[1]

current_dir = os.getcwd()
print(current_dir)

os.chdir(to_dir)

new_dir = os.getcwd()
print(new_dir)
