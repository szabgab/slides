print(2 > 1) # True
print(0 > 1) # False
print()

# comparing different types does not make sense
print([2, 3] > 1) # True
print([0, 0] > 1) # True
print()

# compare each element with the scalar and then check if 'all' were True
print(all(map(lambda x: x > 1, [2, 3])))  # True
print(all(map(lambda x: x > 1, [1, 3])))  # False
