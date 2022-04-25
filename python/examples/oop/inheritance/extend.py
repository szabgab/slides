class Parent():
    def greet(self):
        print("Hello World")

class Child(Parent):
    def greet(self):
        print("Hi five!")
        super().greet()
        print("This is my world!")

p = Parent()
p.greet()
print()

c  = Child()
c.greet()
