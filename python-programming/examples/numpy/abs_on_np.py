import numpy as np

a = np.array([[-1, 2, -3], [-4, 5, -7]])
print(a)
print(a.dtype)
abs_a = np.absolute(a)
print(abs_a)
print(abs_a.dtype)

# absolute = np.vectorize(abs)

