import numpy as np
import re

names = np.array(['Mary', 'Bar', 'Joe', 'Jane'])
print(names)
print()


names_with_ar_selector = np.vectorize(lambda x: True if re.search(r'ar', x) else False)
names_with_ar_bool = names_with_ar_selector(names)
print(names_with_ar_bool)
print()

scores = np.array([
    [23, 37, 18, 97, 13, 40],
    [10, 15, 20, 30, 39, 50],
    [99, 20, 83, 42, 19, 31],
    [19, 11, 55, 78, 39, 27]
])

print(scores[names_with_ar_bool])
print()

print(scores[names_with_ar_selector(names)])
