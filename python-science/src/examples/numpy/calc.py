import numpy as np

matrix = np.array([
    [2, 3, 17],
    [27, 1, 10],
])

print(matrix.shape)
print(matrix.sum(axis = 1))
print(matrix.sum(axis = 0))