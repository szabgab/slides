try:
    raise Exception('foo', 'bar', 19, 23)
except Exception as e:
    print(type(e)) # <type 'exceptions.Exception'>
    print(e.args)  # ('foo', 'bar', 19, 23)
    a, b, x, y = e.args
    print(a + b)   # foobar
    print(x + y)   # 42

