def f(name, **kw):
    print(name)
    print(kw)

f(name="Foo", a = 23, b = 12)

# Foo
# {'a': 23, 'b': 12}
