import numpy as np

def fibo(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b

print(fibo(12))
print(fibo.__class__.__name__)

vfibo = np.vectorize(fibo)
a = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    ])
print(vfibo.__class__.__name__)

print(a)
print(a.dtype)
print()

b = vfibo(a)
print(b)
print(b.dtype)
