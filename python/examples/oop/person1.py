class Person:
    name = 'Joseph'

print(Person.name)    # Joseph

Person.name = 'Joe'
print(Person.name)    # Joe

Person.email = 'joe@foobar.com'
print(Person.email)   # joe@foobar.com

x = Person()
print(Person.name)    # Joe
print(Person.email)   # joe@foobar.com
