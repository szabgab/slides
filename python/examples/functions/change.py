a = 42     # number or string
b = a      # This is a copy
print(a)   # 42
print(b)   # 42
a = 1
print(a)   # 1
print(b)   # 42

a = (1, 2)   # tuple
b = a        # this is a copy
print(a)     # (1, 2)
print(b)     # (1, 2)
# a[0] = 42  TypeError: 'tuple' object does not support item assignment
a = (3, 4, 5)
print(a)     # (3, 4, 5)
print(b)     # (1, 2)

