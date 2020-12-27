from collections import namedtuple

Person = namedtuple('Person', ['name', 'email'])

one = Person(name='Joe', email='joe@example.com')
two = Person(name='Jane', email='jane@example.com')

print(one.name)
print(two.email)
