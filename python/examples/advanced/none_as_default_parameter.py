def f(a, b = None):
    if b == None:
         b = []
    b.append(a)
    return b

print(f(1))
print(f(2))
print(f(3))

