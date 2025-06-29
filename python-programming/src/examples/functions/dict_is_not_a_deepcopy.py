def f(**kw):
    print(kw)
    print(hex(id(kw['z'])))
    kw['z']['a'] = 7

z = {'a': 1, 'b': 2}
print(z)
print(hex(id(z)))
f(z = z)

print(z)
