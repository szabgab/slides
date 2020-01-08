class Person:
    pass

# Assign to class attribute and fetch from it
Person.name = 'Joe'
print(Person.name)    # Joe

# Instance object inherits attributes from class objects
x = Person()
print(x.name)         # Joe
y = Person()
print(y.name)         # Joe

# Changes to class attribute are reflected in existing instances as well
Person.name = 'Bar'
print(Person.name)    # Bar
print(x.name)         # Bar

# Creating and setting the instance attribute does not impact the class attribute
x.name = 'Joseph'
print(x.name)         # Joseph
print(Person.name)    # Bar
# Nor does it impact the instance attribute of other instances:
print(y.name)         # Bar

print(x.__dict__)       # {'name': 'Joseph'}
print(y.__dict__)       # {}
print(Person.__dict__)
       # {..., 'name': 'Bar'}
