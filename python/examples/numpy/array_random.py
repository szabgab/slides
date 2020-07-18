import numpy as np

a = np.random.random((2, 5))  # in the range [0.0, 1.0)
print(a)
print()

rng = np.random.default_rng()
b = rng.random(size=(3, 4))
print(b)
