def f(a, b = []):
    b.append(a)
    return b

print(f(1))
print(f(2))
print(f(3))

