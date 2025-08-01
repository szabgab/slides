import __builtin__

def xx(name):
    print("hello")
__builtin__.__import__ = xx;

print('body')
def f():
    print("in f")
