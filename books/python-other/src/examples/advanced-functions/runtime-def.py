import random

def foo():
    return random.random()


print(foo())
print(foo())

def bar(a, b = foo()):
   return [a, b]

print(bar(1))
print(bar(2))
