import numpy as np

a = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34])
print(a)       # [ 1 1 2 3 5 8 13 21 34]

b = a[2:5]
print(b)  # [2 3 5]

a[2] = 20
print(a)       # [ 1 1 20 3 5 8 13 21 34]
print(b)       # [20 3 5]
