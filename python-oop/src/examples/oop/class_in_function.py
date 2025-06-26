def creator():
    class MyClass:
        def __init__(self):
            print('__init__ of MyClass')

    print('before creating instance')
    o = MyClass()
    print(o)
    print(o.__class__.__name__)

creator()

# before creating instance
# __init_ of MyClass
# <__main__.creator.<locals>.MyClass object at 0x7fa4d8d581c0>
# MyClass

# Cannot use it outside of the function:
# MyClass()  # NameError: name 'MyClass' is not defined
