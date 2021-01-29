import functools

def before_one(func):
    def wrapper():
        print("Before")
        func()
    return wrapper

def before_two(func):
    @functools.wraps(func)
    def wrapper():
        print("Before")
        func()
    return wrapper

@before_one
def hello():
    print("Hello")

@before_two
def hi():
    print("Hi")


hello()
print(hello)

hi()
print(hi)
