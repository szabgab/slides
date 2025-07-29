from functools import partial

val = '101010'
print(int(val, base=2))

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo(val))

# Based on example from https://docs.python.org/3/library/functools.html
