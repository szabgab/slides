v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8]

v3 = v1 + v2
print(v3)          # [1, 3, 5, 9, 2, 6, 4, 8]

sums = map(lambda x,y: x+y, v1, v2)
print(sums)        # <map object at 0x7f8fb4cb9748>
print(list(sums))  # [3, 9, 9, 17]

