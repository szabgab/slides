import numpy as np

scores = np.array([
    [23, 37, 18, 97, 13, 40],
    [10, 15, 20, 30, 39, 50],
    [99, 20, 83, 42, 19, 31],
    [19, 11, 55, 78, 39, 27]
])
filename = 'scores.npy'
np.save(filename, scores)

s = np.load(filename)
print(s)
