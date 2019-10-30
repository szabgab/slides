def number():
    yield 42
    yield 19
    yield 23

n = number()
print(type(n))   # <type 'generator'>
print(n.next())  # 42
print(n.next())  # 19
print(n.next())  # 23
print(n.next())  # StopIteration exception
