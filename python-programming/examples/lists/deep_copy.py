from copy import deepcopy

x = ['apple', 'bob', 'cat', 'drone']
y = deepcopy(x)

x[0] = 'qqrq'

print(x)    # ['qqrq', 'bob', 'cat', 'drone']
print(y)    # ['apple', 'bob', 'cat', 'drone']
