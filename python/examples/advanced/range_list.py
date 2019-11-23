import sys

rng = range(3, 9, 2)
numbers = list(rng)
print(rng)        # range(3, 9, 2)
print(numbers)    # [3, 5, 7]

print(sys.getsizeof(rng))     # 48
print(sys.getsizeof(numbers)) # 112
