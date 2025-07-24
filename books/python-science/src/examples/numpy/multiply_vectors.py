import numpy as np

a = np.array([3, 4, 7])
b = np.array([6, 5, 2])
print(a) # [3 4 7]
print(b) # [6 5 2]

c = np.multiply(a, b)
print(c) # [18 20 14]

d = np.dot(a, b)
print(d)   # 52

m = np.matmul(a, b)
print(m)   # 52

