def f(op, count=0, *things, **kw):
    print(op)
    print(count)
    print(things)
    print(kw)

f(2, 3, 4, 5, a=23, b=12)
