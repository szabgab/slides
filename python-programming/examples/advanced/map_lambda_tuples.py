numbers = [1, 2, 3, 4]

pairs = map(lambda n: (n, 2*n), numbers)
print(pairs)

for pair in pairs:
    print(pair)
