print(2 > 1) # True
print(0 > 1) # False
print()

# Comparing different types does not make sense, but nevertheless Python 2 would still do it.
# Python 3 raises exception:
# TypeError: '>' not supported between instances of 'list' and 'int'
# print([2, 3] > 1) # True
# print([0, 0] > 1) # True
# print()

# compare each element with the scalar and then check if 'all' were True
print(all(map(lambda x: x > 1, [2, 3])))  # True
print(all(map(lambda x: x > 1, [1, 3])))  # False
