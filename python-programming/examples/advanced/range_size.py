import sys

for ix in (range(21)):
    rng = range(ix)
    numbers = list(rng)
    print("{:>3} {:>3} {:>4}".format(ix, sys.getsizeof(rng), sys.getsizeof(numbers)))
