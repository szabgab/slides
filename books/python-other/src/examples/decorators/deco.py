#from inspect import getmembers, isfunction
import inspect


def change(sub):
    def new(*args, **kw):
        print("before")
        res = sub(*args, **kw)
        print("after")
        return res
    return new

def add(x, y):
    return x+y

#print(add(2, 3))

fixed = change(add)
#print(fixed(3, 4))

def replace(subname):
    def new(*args, **kw):
        print("before")
        res = locals()[subname](*args, **kw)
        print("after")
        return res
    locals()[subname] = new

replace('add')
add(1, 7)

def say():
    print("hello")

#print(dir())
#getattr('say')


