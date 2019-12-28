def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    i = 0
    while i+1 < len(iterable):
        t = (iterable[i], iterable[i+1])
        i += 2
        yield t

l = [1, 2, 3, 4, 5, 6]
for x, y in pairwise(l):
   print "%d + %d = %d" % (x, y, x + y)


