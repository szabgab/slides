from my_module2 import *

print(a())     # in a
print(_c())    # in _c

print(b)

# Traceback (most recent call last):
#   File ".../examples/modules/z.py", line 7, in <module>
#     print(b)       # value of b
# NameError: name 'b' is not defined
