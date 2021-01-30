def tron(prefix):
    def real_tron(func):
        def new_func(v):
            print("{} Calling {}({})".format(prefix, func.__name__, v))
            return func(v)
        return new_func
    return real_tron
