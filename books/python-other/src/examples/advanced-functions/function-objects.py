
c = 0

def foo():
   global c
   c += 1
   return c


print(foo())   # 1
print(foo())   # 2
x = foo           # assigning the function object
y = foo()         # assigning the return value of the function
print(foo())   # 4
print(x())     # 5
print(y)       # 3



