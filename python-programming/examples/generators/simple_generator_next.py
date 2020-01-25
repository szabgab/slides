def number():
    yield 42
    yield 19
    yield 23

n = number()
print(type(n))
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
