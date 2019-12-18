print(2 > 1) # True
print(0 > 1) # False
print()

numbers = [2, 4]
# Comparing different types does not make sense, but nevertheless Python 2 would still do it.
# Python 3 raises exception:
# TypeError: '>' not supported between instances of 'list' and 'int'
# print(numbers > 1) # True
# print(numbers > 7) # True
# print()

# compare each element with the scalar and then check if 'all' were True
print(all(map(lambda x: x > 1, numbers)))  # True
print(all(map(lambda x: x > 2, numbers)))  # False
