class Person():
    name = 'abc'

    def __init__(self):
        self.name = 'qqrq'

    def show(self):
        print(Person.name)

print(Person.name)    # abc

Person.name = 'Foo'
print(Person.name)    # Foo

x = Person()
x.show()              # Foo
print(x.name)         # qqrq
print(Person.name)    # Foo

Person.name = 'Bar'
print(x.name)         # qqrq
print(Person.name)    # Bar
x.show()              # Bar

x.name = 'Zorg'       # creating and setting the instance attribute
print(x.name)         # Zorg
print(Person.name)    # Bar

x.show()              # Bar
