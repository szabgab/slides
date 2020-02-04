import random

def alloc():
    a = {
        'data': str(random.random()) + "a" * 10000000,
    }
    b = {
        'data': str(random.random()) + "b" * 10000000,
    }
    a['other'] = b
    b['other'] = a

