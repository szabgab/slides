def tron(func):
    def new_func(*args, **kw):
        params = list(args)
        for (k, v) in kw.items():
            params.append(f"{k}={v}")
        print("Calling {}({})".format(func.__name__, ', '.join(params)))
        return func(*args, **kw)
    return new_func

