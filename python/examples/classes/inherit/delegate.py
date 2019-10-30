class Parent(object):
    def greet(self):
        print("Hello", self.get_name())

class Child(Parent):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

# Should not create instance from Parent
# p = Parent()
# p.greet()    # AttributeError: 'Parent' object has no attribute 'get_name'

c  = Child('Foo')
c.greet()    # Hello Foo
