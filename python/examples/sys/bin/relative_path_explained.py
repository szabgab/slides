import os
import sys

print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_root)

mypath = os.path.join(project_root, 'lib')
print(mypath)
sys.path.insert(0, mypath)

import my_module
my_module.run()

