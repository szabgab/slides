class Parent():
    def greet(self):
        print("Hello World")

class Child(Parent):
    pass

p = Parent()
p.greet()    # Hello World

c  = Child()
c.greet()    # Hello World
