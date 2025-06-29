def f(**kw):
    print(kw)
    kw['a'] = 7
    print(kw)

z = 23
f(a=10, b=12)
f(a=z, y=99, z=1)
print(z)
