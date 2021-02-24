import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        return func(*args, **kw)
    return wrapper


@decorator
def zero():
    print("zero")

@decorator
def one(x):
    print(f"one({x})")

@decorator
def two(x, y):
    print(f"two({x, y})")


zero()
one('hello')
two( y = 7, x = 8 )

print(zero)
print(one)
print(two)
