import numpy as np
import re

scores = np.array([
    [23, 37, 18, 97, 13, 40],
    [10, 15, 20, 30, 39, 50],
    [99, 20, 83, 42, 19, 31],
    [19, 11, 55, 78, 39, 27]
])
print(scores)
print()

high_scores_boolean = (scores > 20)
print(high_scores_boolean)
print()

high_scores = scores[high_scores_boolean]
print(high_scores)
