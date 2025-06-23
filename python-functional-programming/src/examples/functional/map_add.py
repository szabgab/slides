v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8]

v3 = v1 + v2
print(v3)

sums = map(lambda x,y: x+y, v1, v2)
print(sums)
print(list(sums))
