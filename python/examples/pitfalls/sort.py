from __future__ import print_function

mixed = [10, '1 foo', 42, '4 bar']
print(mixed)  # [100, 'foo', 42, 'bar']
mixed.sort()
print(mixed)  # [42, 100, 'bar', 'foo']


