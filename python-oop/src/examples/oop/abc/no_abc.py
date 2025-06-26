class NotImplementedError(Exception):
    pass

class Base():
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
r.foo()
r.bar()
f = Fake()
f.foo()
f.bar()
