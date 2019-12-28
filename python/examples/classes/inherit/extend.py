class Parent():
    def greet(self):
        print("Hello World")

class Child(Parent):
    def greet(self):
        print("Hi five!")
        super().greet()
        print("This is my world!")

p = Parent()
p.greet()    # Hello World

c  = Child()
c.greet()

# Hi five!
# Hello World
# This is my world!
