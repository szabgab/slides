import sys

rng = range(3, 9, 2)
numbers = list(rng)
print(rng)        # range(3, 9, 2)
print(numbers)    # [3, 5, 7]

others = list(range(2, 11, 3))
print(others)   # [2, 5, 8]

print(sys.getsizeof(rng))     # 48
print(sys.getsizeof(numbers)) # 112


