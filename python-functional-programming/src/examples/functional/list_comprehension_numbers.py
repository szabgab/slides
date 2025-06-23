numbers = [1, 3, 2, 4]

t = filter(lambda n: n > 2, numbers)
print(t)  # [3, 4]

n1 = map(lambda n: n*n, t)
print(n1) # [9, 16]


n2 = map(lambda n: n*n, filter(lambda n: n > 2, numbers))
print(n2)  # [9, 16]



n3 = [ n*n for n in numbers if n > 2 ]
print(n3) # [9, 16]
