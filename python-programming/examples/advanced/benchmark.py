import timeit

import random
chars = []
for i in xrange(200):
    chars.append(chr(65 + random.randrange(0, 26)))

print(timeit.timeit('str = "".join(chars)',
    setup="from __main__ import chars", number=10000))

print(timeit.timeit('reduce(lambda x, y: x+y, chars)',
    setup="from __main__ import chars", number=10000))
