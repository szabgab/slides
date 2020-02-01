class Person():
    name = 'Joseph'

    def __init__(self, given_name):
        self.name = given_name

    def show_class(self):
        return Person.name

    def show_instance(self):
        return self.name

print(Person.name)        # Joseph

Person.name = 'Classy'
print(Person.name)     # Classy
# print(Person.show_class()) # TypeError: show_class() missing 1 required positional argument: 'self'

x = Person('Joe')
print(x.name)             # Joe
print(Person.name)        # Classy
print(x.show_class())     # Classy
print(x.show_instance())  # Joe

Person.name = 'General'
print(x.name)             # Joe
print(Person.name)        # General
print(x.show_class())     # General
print(x.show_instance())  # Joe

x.name = 'Zorg'           # changing the instance attribute
print(x.name)             # Zorg
print(Person.name)        # General
print(x.show_class())     # General
print(x.show_instance())  # Zorg
