class Parent():
    def greet(self):
        print("Hello World")

class Child(Parent):
    def greet(self):
        print("Hi five!")

p = Parent()
p.greet()    # Hello World

c  = Child()
c.greet()    # Hi five!
