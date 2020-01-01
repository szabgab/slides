from abc import ABCMeta, abstractmethod

#class Base(metaclass = ABCMet):
class Base():
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


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
f = Fake()
   # TypeError: Can't instantiate abstract class Fake with abstract methods bar
