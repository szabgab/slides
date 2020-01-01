class Person():
    def __init__(self, txt):
        self.name = txt

    def show(self):
        print(self.name)

x = Person('Foo')
y = Person('Bar')
x.show()              # Foo
y.show()              # Bar

def hello(obj):
    print("Hello " + obj.name)

z = x.show
z()                   # Foo

Person.show = hello
x.show()             # Hello Foo
y.show()             # Hello Bar
