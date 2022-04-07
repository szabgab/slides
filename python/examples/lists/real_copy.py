x = ['apple', 'bob', 'cat', 'drone']
z = x[:]

x[0] = 'qqrq'

print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(z)    # ['apple', 'bob', 'cat', 'drone']
