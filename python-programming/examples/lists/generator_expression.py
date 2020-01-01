#!/usr/bin/env python
import sys

l = [n*2 for n in xrange(1000)] # List comprehension
g = (n*2 for n in xrange(1000)) # Generator expression

for v in l:
    pass
for v in g:
    pass

print(sys.getsizeof(l))  # 9032
print(sys.getsizeof(g))  # 80

print(type(l))  # <type 'list'>
print(type(g))  # <type 'generator'>

print(l[4])   # 8
#print(g[4])   # TypeError: 'generator' object has no attribute '__getitem__'
