def fib(n):
#    if n < 1:
#        raise ValueError(f'Invalid parameter {n}')
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a+b
    return a

