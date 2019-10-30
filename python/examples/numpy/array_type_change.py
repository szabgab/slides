import numpy as np

a = np.array([3, 4, 7])
print(a.dtype) # int64
print(a.shape)  # (3,)

x = (a / 2)
print(x)        # [ 1.5  2.   3.5]
print(x.dtype)  # float64
print(x.shape)  # (3,)
