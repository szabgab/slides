import os, sys

# import my_module   # ImportError: No module named my_module

print(__file__)   # examples/sys/bin/relative_path.py
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

mypath = os.path.join(project_root, 'lib')
print(mypath) # /Users/gabor/work/training/python/examples/sys/../lib
sys.path.insert(0, mypath)

import my_module   # Importing my_module

