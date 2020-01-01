class Base(object):
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Real(Base):
    def foo(self):
        print('foo in Real')
    def bar(self):
        print('bar in Real')
    def other(self):
        pass

class Fake(Base):
    def foo(self):
        print('foo in Fake')

r = Real()
r.foo()    # foo in Real
r.bar()    # bar in Real
f = Fake()
f.foo()    # foo in Fake
f.bar()    # NotImplementedError
