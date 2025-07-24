def fib(n):
    if n < 1:
        raise ValueError(f'Invalid parameter was given {n}')
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, a+b
    return a

def add(x, y):
    return x + y

def area(x, y):
    if x > 0 and y > 0:
        return x * y
    else:
        return None
