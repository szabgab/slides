from itertools import izip

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

l = [1, 2, 3, 4, 5, 6, 7]
for x, y in pairwise(l):
   print("{} + {} = {}".format(x, y, x + y))

# 1 + 2 = 3
# 3 + 4 = 7
# 5 + 6 = 11
