import sys

print('mod' in sys.modules) # False

import mod
print('mod' in sys.modules)  # True
print(sys.modules['mod'])
     # <module 'mod' from '/stuff/python/examples/modules/mod.py'>

print(sys.modules["sys"])    # <module 'sys' (built-in)>
