import numpy as np

c = np.ones(4, dtype='int32')
print(c)          # [1 1 1 1]
print(c.dtype)    # int32
print(c.shape)    # (4,)
print()


d = np.zeros(3, dtype='float32')
print(d)          # [ 0.  0.  0.]
print(d.dtype)    # float32
print(d.shape)    # (3,)
print()


a = np.ones([2, 3])
print(a)
# [[1., 1., 1.],
# [1., 1., 1.]]
print(a.dtype)    # float64
print(a.shape)    # (2, 3)
