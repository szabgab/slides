def grouped(iterable, n):
    """s -> (s0,s1,s2,...sn-1),
          (sn,sn+1,sn+2,...s2n-1),
          (s2n,s2n+1,s2n+2,...s3n-1), ..."""

    i = 0
    while i+n-1 < len(iterable):
        t = tuple(iterable[i:i+n])
        i += n
        yield t

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x, y, z in grouped(l, 3):
    print("{} + {} + {} = {}".format(x, y, z, x + y + z))

