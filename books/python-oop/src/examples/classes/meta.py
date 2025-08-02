class M(type):
    pass

class A(object):
    pass

class B(object):
    __metaclass__ = M

a = A()
print(type(a))
b = B()
print(type(b))



class Meta(type):
    def __init__(self, *args, **kwargs):
        print('Meta.__init__')
        print(self)   # <class '__main__.C'>
        print(args)   # ('C', (<type 'object'>,),
                      # {'__module__': '__main__',
                      #  '__metaclass__': <class '__main__.Meta'>})
        print(kwargs) # {}

class C(object):
    __metaclass__ = Meta

c = C()
print(type(c))

class MyABC(type):
    def __init__(self, *args):
        print('Meta.__init__')
        print(args)   # ('C', (<type 'object'>,),
                      # {'__module__': '__main__',
                      # '__metaclass__': <class '__main__.Meta'>})

class Base(object):
    __metaclass__ = MyABC
