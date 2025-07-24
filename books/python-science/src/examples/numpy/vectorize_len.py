import numpy as np

animals = np.array(['Cow', 'Elephant', 'Snake', 'Camel', 'Praying Mantis'])
print(animals)

vlen = np.vectorize(len)
print(vlen(animals))
