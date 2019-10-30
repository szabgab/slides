x = ['abc', 'def']
print(x)     # ['abc', 'def']

y = [x, 'xyz']
print(y)          # [['abc', 'def'], 'xyz']
print(y[0])       #  ['abc', 'def']

print(x[0])       #    abc
print(y[0][0])    #    abc

