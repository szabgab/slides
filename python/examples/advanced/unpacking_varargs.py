def f(*args, **kwargs):
    print('f: ', args)
    print('f: ', kwargs)
    g(*args, **kwargs)

def g(*args, **kwargs):
    print('g: ', args)
    print('g: ', kwargs)

f(1, 2, a=3, b=4)


