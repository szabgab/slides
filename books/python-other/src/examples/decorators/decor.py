def tron(func):
    def new_func(v):
        print(f"Calling {func.__name__}({v})")
        return func(v)
    return new_func
