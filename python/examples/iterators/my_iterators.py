def fibo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def alter():
    n = 1
    while True:
       yield n
       if n < 0:
           n -= 1
       else:
           n += 1
       n *= -1
