import random

def foo():
    return random.random()

print foo()
print foo()

def bar(a, b = foo()):

    def inner_func(x, y = foo()):
        return [x, y]

    print 'inner', inner_func(a)
    return [a, b]

print bar(1)
print bar(2)

