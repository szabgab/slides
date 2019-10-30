def tron(func):
    def new_func(v):
        print("Calling {}({})".format(func.__name__, v))
        return func(v)
    return new_func
