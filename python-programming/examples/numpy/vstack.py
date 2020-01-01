import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])
print(a)    # [1 2 3]
print(b)    # [4 5 6]
print(c)    # [7 8 9]

m = np.vstack([a, b])
print(m)

# [[1 2 3]
#  [4 5 6]]

d3 = np.vstack([m, c])
print(d3)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]



