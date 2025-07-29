
functions = []

def register(func):
    global functions
    functions.append(func.__name__)

    return func

@register
def f():
    print("in f")

print(functions)

