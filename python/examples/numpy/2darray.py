import numpy as np

a = np.array([
    [ 1,  2,  3,  4,  5],
    [ 2,  3,  4,  5,  6]
])

print(a)
# [[1 2 3 4 5]
#  [2 3 4 5 6]]

print(a.shape) # (2, 5)
print(a.ndim)  # 2


print(a * 3)
# [[ 3  6  9 12 15]
#  [ 6  9 12 15 18]]

print(a + 7)
# [[ 8  9 10 11 12]
#  [ 9 10 11 12 13]]
