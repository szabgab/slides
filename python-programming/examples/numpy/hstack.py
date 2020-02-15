import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
print(a)
print(b)
print(c)
print()

d = np.hstack([a, b])
print(d)
print()

e = np.hstack([d, c])
print(e)
