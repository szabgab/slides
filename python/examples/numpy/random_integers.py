import numpy as np

a = np.random.randint(10, size=(3, 4))
print(a)

rng = np.random.default_rng()
b = rng.integers(42, size=(3, 4))
print(b)
