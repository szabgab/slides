import numpy as np

def fibo(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b

vfibo = np.vectorize(fibo)
a = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    ])
print(a)
print(a.dtype)
print()

b = vfibo(a)
print(b)
print(b.dtype)
