numbers  = [0, 1, 2, 3]

gn = (n*n for n in numbers)
print(gn)

for num in gn:
    print(num)


gn = (n*n for n in numbers)
print(list(gn))

print(list(gn))
