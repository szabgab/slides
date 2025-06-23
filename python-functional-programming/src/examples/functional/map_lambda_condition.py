numbers = [1, 2, 3, 4]

a = map(lambda n: 2*n if n % 2 else n, numbers)
print(a)   # [2, 2, 6, 4]
