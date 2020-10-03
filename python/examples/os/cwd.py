import os

this_dir = os.getcwd()
print(this_dir)

# os.chdir('/path/to/some/dir')
os.chdir('..')

new_dir = os.getcwd()
print(new_dir)
