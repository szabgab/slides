def number():
    yield 42
    yield 19
    yield 23

num = number()
print(type(num))
for n in num:
    print(n)
