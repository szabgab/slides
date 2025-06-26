import inspect

class Base():
    def __init__(self, *args, **kwargs):
        if self.__class__.__name__ == 'Base':
            raise Exception('You are required to subclass the {} class'
                .format('Base'))

        methods = set([ x[0] for x in
            inspect.getmembers(self.__class__, predicate=inspect.ismethod)])
        required = set(['foo', 'bar'])
        if not required.issubset( methods ):
            missing = required - methods
            raise Exception("Requried method '{}' is not implemented in '{}'"
                .format(', '.join(missing), self.__class__.__name__))


class Real(Base):
    def foo(self):
        print('foo in Real')
    def bar(self):
        print('bar in Real')
    def other(self):
        pass

class Fake(Base):
# user can hide the __init__ method of the parent class:
#    def __init__(self):
#        pass
    def foo(self):
        print('foo in Fake')

r = Real()
#b = Base()  # You are required to subclass the Base class
#f = Fake()  # Requried method 'bar' is not implemented in class 'Fake'
