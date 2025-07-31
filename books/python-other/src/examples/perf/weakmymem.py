import random
import weakref

def alloc():
    a = {
        'data': str(random.random()) + "a" * 10000000,
    }
    b = {
        'data': str(random.random()) + "b" * 10000000,
    }
    #a['other'] = weakref.WeakKeyDictionary(b)
    z = weakref.ref(b)
    #a['other'] = 
    #weakref.ref(a['other'])
    #b['other'] = a
    #weakref.ref(b['other'])
