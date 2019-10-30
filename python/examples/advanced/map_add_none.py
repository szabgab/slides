v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8, 10]

print(map(lambda x,y: (0 if x is None else x) + (0 if y is None else y), v1, v2))
# [3, 9, 9, 17, 10]
