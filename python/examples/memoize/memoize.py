def memoize(f):
    def caching(n):
        key = n
        if 'data' not in caching.__dict__:
            caching.data = {}
        if key not in caching.data:
            caching.data[key] = f(n)
        return caching.data[key]

    return caching

