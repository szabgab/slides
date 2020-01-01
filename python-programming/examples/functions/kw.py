def f(op, *things, **kw):
    print(op)
    print(things)
    print(kw)

f(2, 3, 4, a = 23, b = 12)

# 2
# (3, 4)
# {'a': 23, 'b': 12}
