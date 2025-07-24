v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8, 10]

print(map(lambda x,y: (x or 0) + (y or 0), v1, v2))
# [3, 9, 9, 17, 10]
