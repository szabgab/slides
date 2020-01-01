import sys

for i in (range(21)):
    rng = range(i)
    numbers = list(rng)
    print("{:>3} {:>3} {:>4}".format(i, sys.getsizeof(rng), sys.getsizeof(numbers)))
