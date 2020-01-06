import sys

lst = [n*2 for n in range(1000)] # List comprehension
gen = (n*2 for n in range(1000)) # Generator expression

for val in lst:
    pass
for val in gen:
    pass

print(sys.getsizeof(lst))  # 9024
print(sys.getsizeof(gen))  # 120

print(type(lst))  # <type 'list'>
print(type(gen))  # <type 'generator'>

print(lst[4])   # 8
print(gen[4])   # TypeError: 'generator' object has no attribute '__getitem__'
