import numpy as np

scores = np.array([23, 37, 18, 97, 13, 40])
print(scores.sum())          # 228
print(len(scores))           # 6
print(scores.mean())         # 38.0

print(scores.std())          # 28.0950766743 standard deviation
print(scores.var())          # 789.333333333 variance
print(np.median(scores))     # 30.0
print(scores.max())          # 97
print(scores.min())          # 13

print(scores.cumsum())       # [ 23  60  78 175 188 228]
