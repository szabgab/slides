def tron(func):
    def new_func(*args, **kwargs):
        print("Calling {}({}, {})".format(func.__name__, args, kwargs))
        out = func(*args, **kwargs)
        print("Finished {}({})".format(func.__name__, out))
        return out
    return new_func
