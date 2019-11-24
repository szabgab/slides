v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8, 10]

sums = map(lambda x,y: x+y, v1, v2)
print(sums)  # <map object at 0x7fa7bf3d2e48>

print(list(sums))
