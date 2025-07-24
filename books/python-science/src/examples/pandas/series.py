import pandas

s = pandas.Series([1, 1, 2, 3, 5, 8])
print(s)

# 0    1
# 1    1
# 2    2
# 3    3
# 4    5
# 5    8
# dtype: int64

print(s.values)  # [1 1 2 3 5 8]
print(s.index)   # RangeIndex(start=0, stop=6, step=1)

print('----')
print(s.sum())      # 20
print(s.count())    # 6
print(s.mean())     # 3.33333333333
print(s.median())   # 2.5
print(s.std())      # 2.73252020426
print(s.cumsum())

# 0     1
# 1     2
# 2     4
# 3     7
# 4    12
# 5    20
# dtype: int64
