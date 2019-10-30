import inspect
class MyABC(type):
    def __init__(class_object, *args):
        #print('Meta.__init__')
        #print(class_object)
        #print(args)
            # ('Base',
            # (<type 'object'>,),
            # {
            #   '__required_methods__': ['foo', 'bar'],
            #   '__module__': '__main__',
            #   '__metaclass__': <class '__main__.MyABC'>
            # })
#        attr = dict(args)
        if not '__metaclass__' in args[2]:
            return

        if not '__required_methods__' in args[2]:
             raise Exception("No __required_methods__")
        name = args[0]
        required_methods = set(args[2]['__required_methods__'])
        def my_init(self, *args, **kwargs):
            if self.__class__.__name__ == name:
                raise Exception("You are required to subclass the '{}' class"
                    .format(name))

            #print("my_init")
            methods = set([ x[0] for x in
                inspect.getmembers(self.__class__, predicate=inspect.ismethod)])
            if not required_methods.issubset( methods ):
                missing = required_methods - methods
                raise Exception("Requried method '{}' is not implemented in '{}'"
                    .format(', '.join(missing), self.__class__.__name__))

        class_object.__init__ = my_init


class Base(object):
    __metaclass__ = MyABC
    __required_methods__ = ['foo', 'bar']

# b = Base() # Exception: You are required to subclass the 'Base' class

class Real(Base):
    def foo():
        pass
    def bar():
        pass

r = Real()

class Fake(Base):
    def foo():
        pass

#f = Fake() # Exception: Requried method 'bar' is not implemented in class 'Fake'

class UnFake(Fake):
    def bar():
        pass

uf = UnFake()
