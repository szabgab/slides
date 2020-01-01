def f(a, b=1, *args, **kwargs):
    print('a:     ', a)
    print('b:     ', b)
    print('args:  ', args)
    print('kwargs:', kwargs)
    return a + b

f(2, 3, 4, 5, c=6, d=7)
print()
f(2, c=5, d=6)
print()
f(10)
