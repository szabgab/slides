import sys

numbers  = [0, 1, 2, 3, 4, 5, 6]

gn = (n*n for n in numbers)
print(gn)
print(sys.getsizeof(gn))
print()

for num in gn:
    print(num)
print()

gn = (n*n for n in numbers)
squares = list(gn)
print(sys.getsizeof(squares))
print(squares)

print(list(gn)) # the generator was already exhausted
