numbers = [1, 2, 3, 4]

pairs = map(lambda n: (n, 2*n), numbers)
print(pairs)   # <map object at 0x7f07e5e47940>

for pair in pairs:
    print(pair)

# (1, 2)
# (2, 4)
# (3, 6)
# (4, 8)

