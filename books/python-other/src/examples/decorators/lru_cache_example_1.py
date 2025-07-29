import functools

@functools.lru_cache(maxsize=3)
def compute(x, y):
    print(f"Called with {x} and {y}")
    # some long computation here
    return x+y

compute(1, 2) # Called with 1 and 2
compute(1, 2)
compute(1, 2)

compute(1, 3) # Called with 1 and 3
compute(1, 3)

compute(1, 4) # Called with 1 and 4
compute(1, 4)

compute(1, 5) # Called with 1 and 5

compute(1, 2) # Called with 1 and 2
compute(1, 2)

