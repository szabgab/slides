import numpy as np

a = np.array([True, True, False])
print(a.dtype)
print(a)
print()

not_a = np.logical_not(a)
print(not_a.dtype)
print(not_a)
print()

b = np.array([True, True, False, 0, 42])
print(b.dtype)
print(b)
print()

not_b = np.logical_not(b)
print(not_b.dtype)
print(not_b)
print()
