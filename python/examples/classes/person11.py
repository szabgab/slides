class Person:
    name = 'Joe'

# Class Attributes are inherited by object instances when accessing them.
x = Person()
print(x.name)         # Joe
y = Person()
print(y.name)         # Joe

# Changes to class attribute are reflected in existing instances as well
Person.name = 'Bar'
print(Person.name)    # Bar
print(x.name)         # Bar

# Setting the attribute via the instance will create an instance attribute that
# shadows the class attribute
x.name = 'Joseph'
print(x.name)         # Joseph
print(Person.name)    # Bar
# Nor does it impact the instance attribute of other instances:
print(y.name)         # Bar

# Both instance and class have a dictionary containing its members:
print(x.__dict__)       # {'name': 'Joseph'}
print(y.__dict__)       # {}
print(Person.__dict__)  # {..., 'name': 'Bar'}
