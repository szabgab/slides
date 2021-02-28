distances = c(11, 12, 13, 14, 15, 16, 17, 18)

print(distances[c(2, 4)])  # 12, 14
print(distances[2:4])  # 12, 13, 14


locations = c(5, 3, 5, 7)
nd = distances[locations]

print(nd)            # 15, 13, 15, 17
print(distances)
