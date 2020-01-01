#!/usr/bin/env python
from __future__ import print_function
import sys

r = range(1000)
x = xrange(1000)

for v in r:   # 0..999
    pass
for v in x:   # 0..999
    pass

print(sys.getsizeof(r))  # 8072
print(sys.getsizeof(x))  # 40
