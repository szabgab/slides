import decor_param

@decor_param.tron('foo')
def fibo(n):
    if n in (1,2): return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(5))
