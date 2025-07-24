def f(n):
    if int(n) != n or n < 0:
        raise ValueError("Bad parameter")

    if n == 0:
       return 1
    return n * f(n-1)

print(f(1))   # 1
print(f(2))   # 2
print(f(3))   # 6
print(f(4))   # 24

f(-1)

