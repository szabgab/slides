def double(n):
    return 2*n

numbers = [1, 2, 3, 4]
d = map(double, numbers)
print(d)                         # [2, 4, 6, 8]

name = "FooBar"
x = map(double, name)
print(x)  # ['FF', 'oo', 'oo', 'BB', 'aa', 'rr']
