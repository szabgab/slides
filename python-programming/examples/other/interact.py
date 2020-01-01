
def f(a, b):
    c = a + b
    d = a * b
    return c+d

def run():
    print(f(2, 3))

    import code
    code.interact(local=locals())

    print(f(19, 23))

run()
