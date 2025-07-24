import functools

def add_debug(cls, method):
    original = getattr(cls, method)
    @functools.wraps(original)
    def debug(*args, **kwargs):
        print("Before method")
        result = original(*args, **kwargs)
        print("After method")
        return result
    setattr(cls, method, debug)

