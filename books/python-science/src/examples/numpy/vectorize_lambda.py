import numpy as np

animals = np.array(['Cow', 'Elephant', 'Snake', 'Camel', 'Praying Mantis'])
print(animals)

longer_than_5 = np.vectorize(lambda x: len(x) > 5)
long_animals_bool = longer_than_5(animals)
print(long_animals_bool)
