import time
def tron(func):
    def new_func(*args, **kwargs):
        start = time.time()
        print("Calling {}({}, {})".format(func.__name__, args, kwargs))
        out = func(*args, **kwargs)
        end = time.time()
        print("Finished {}({})".format(func.__name__, out))
        print("Elapsed time: {}".format(end - start))
        return out
    return new_func
