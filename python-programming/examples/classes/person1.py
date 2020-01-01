class Person():
    pass

# Assign to class attribute and fetch from it
Person.name = 'Foo'
print(Person.name)    # Foo

# Instance object inherits attributes from class objects
x = Person()
print(x.name)         # Foo
y = Person()
print(y.name)         # Foo

# Changes to class attribute are reflected in existing instances as well
Person.name = 'Bar'
print(Person.name)    # Bar
print(x.name)         # Bar

# Creating and setting the instance attribute does not impact the class attribute
x.name = 'Zorg'
print(x.name)         # Zorg
print(Person.name)    # Bar
print(y.name)         # Bar

# Nor does it impact the instance attribute of other instances:
y.name = 'Qqrq'
print(x.name)         # Zorg
print(Person.name)    # Bar
print(y.name)         # Qqrq

print(x.__dict__)       # {'name': 'Zorg'}
print(y.__dict__)       # {'name': 'Qqrq'}
print(Person.__dict__)
       # {'__module__': '__main__', '__doc__': None, 'name': 'Bar'}
