import timeit

def one_by_one():
    import random
    str = ""
    for i in range(200):
        str += chr(65 + random.randrange(0, 26))
    return str

def at_once():
    import random
    chars = []
    for i in range(200):
        chars.append(chr(65 + random.randrange(0, 26)))
    str = ''.join(chars)
    return str

print(timeit.timeit('one_by_one()',
    setup="from __main__ import one_by_one", number=10000))

print(timeit.timeit('at_once()',
    setup="from __main__ import at_once", number=10000))

