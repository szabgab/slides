from series import integers
from itertools import izip

n3 = integers(3)
n7 = integers(7)
d = ( sum(p) for p in izip(n3, n7) )
for i in d:
    print(i)
    if i >= 40:
        break
