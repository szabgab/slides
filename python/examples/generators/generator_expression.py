import sys

lst = [n*2 for n in range(1000)] # List comprehension
gen = (n*2 for n in range(1000)) # Generator expression

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
print()

print(type(lst))
print(type(gen))
print()

print(lst[4])
print()

print(gen[4])
