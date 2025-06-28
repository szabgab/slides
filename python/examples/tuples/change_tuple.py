
z = ([1, 2], [3, 4])
print(z)               # ([1, 2], [3, 4])

z[0].append(5)
print(z)               # ([1, 2, 5], [3, 4])


# z[0] = [7, 8] # TypeError: 'tuple' object does not support item assignment
# z.append(7)   # AttributeError: 'tuple' object has no attribute 'append'
