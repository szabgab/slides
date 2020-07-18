import sys

numbers  = [0, 1, 2, 3]

sqrs = map(lambda n: n*n, numbers)
print(sqrs)         # <map object at 0x7fdcab2f5940>
print(list(sqrs))   # [0, 1, 4, 9]
print(sys.getsizeof(sqrs))
print()

squares = [n*n for n in numbers]
print(squares)   # [0, 1, 4, 9]
print(sys.getsizeof(squares))
