class Parent():
    def greet(self):
        print("Hello World")

class Child(Parent):
    def greet(self):
        print("Hi five!")

p = Parent()
p.greet()
print()

c  = Child()
c.greet()
