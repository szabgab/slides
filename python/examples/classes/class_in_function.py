def creator():
    class MyClass():
        pass
    o = MyClass()
    print(o.__class__.__name__) # MyClass

creator()
# MyClass()  # NameError: name 'MyClass' is not defined
