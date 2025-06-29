import os
import sys

if len(sys.argv) != 2:
    exit("Usage: {} PATH_TO_DIRECTORY".format(sys.argv[0]))

root = sys.argv[1]

for dirname, dirs, files in os.walk(root):
    #print(dirname)     # relative path (from cwd) to the directory being processed
    #print(dirs)       # list of subdirectories in the currently processed directory
    #print(files)       # list of files in the currently processed directory

    for filename in files:
        print(os.path.join(dirname, filename))   # relative path to the "current" file

