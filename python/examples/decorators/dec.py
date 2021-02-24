
def decor(func):
    print('decor')
    def internal():
        print('internal')
    return internal


@decor
def f():
    print('f')
f()

