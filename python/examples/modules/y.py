from my_module import *

print(a())     # in a
print(b)       # value of b

print(d())     # in d


print(_c())

# Traceback (most recent call last):
#   File ".../examples/modules/y.py", line 9, in <module>
#     print(_c())    # in _c
# NameError: name '_c' is not defined
