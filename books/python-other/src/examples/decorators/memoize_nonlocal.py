def memoize(f):
    data = {}
    def caching(n):
        nonlocal data
        key = n
        if key not in data:
            data[key] = f(n)
        return data[key]

    return caching

