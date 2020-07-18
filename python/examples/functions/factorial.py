def f(n):
    if n == 0:
       return 1
    return n * f(n-1)

print(f(1))   # 1
print(f(2))   # 2
print(f(3))   # 6
print(f(4))   # 24

