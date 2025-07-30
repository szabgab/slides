def f(*args, **kwargs):
    print('f args:   ', args)
    print('f kwargs: ', kwargs)
    g(args, kwargs)

def g(*args, **kwargs):
    print('g args:   ', args)
    print('g kwargs: ', kwargs)

f(1, 2, a=3, b=4)
