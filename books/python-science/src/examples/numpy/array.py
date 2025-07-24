import numpy as np

a = np.array([3, 4, 7])
print(a)         # [3 4 7]
print(a * 3)     # [ 9 12 21]
print(a + 4)     # [ 7  8 11]
print(a.dtype)   # int64
print(a.ndim)    # 1
print(a.shape)   # (3,)

b = np.array([2, 3.14, -1])
print(b.dtype)   # float64
print(b.shape)   # (3,)

c = np.array(['one', 'two', 'three'])
print(c.dtype)   # <U5    (Unicode less than 5 characters)
