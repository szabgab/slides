from functools import reduce

numbers = []

print(reduce(lambda x,y: x+y, numbers))

# TypeError: reduce() of empty sequence with no initial value
