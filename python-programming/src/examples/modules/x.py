from my_module import a,b,_c

print(a())     # in a
print(b)       # value of b
print(_c())    # in _c

print(d())
# Traceback (most recent call last):
#   File ".../examples/modules/x.py", line 7, in <module>
#     print(d())
# NameError: name 'd' is not defined
