import numpy as np

a = np.random.random((2, 5))  # in the range [0.0, 1.0)
print(a)

# [[0.45936721 0.5226969  0.40805708 0.98151515 0.17184473]
#  [0.59632204 0.00875671 0.21438141 0.44184983 0.44205459]]


rng = np.random.default_rng()
b = rng.integers(10, size=(3, 4))
print(b)

# [[2 9 5 5]
#  [9 9 8 3]
#  [9 0 4 0]]

