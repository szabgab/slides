import numpy as np

a = np.array([127], 'int8')
print(a.dtype)   # int8
print(a)         # [127]

a[0] += 1        # [-128]
print(a)

a[0] -= 1        # [127]
print(a)

a[0] = 255
print(a)         # [-1]

a[0] += 1
print(a)         # [0]
