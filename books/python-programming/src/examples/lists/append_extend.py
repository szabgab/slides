names = ['Foo Bar', 'Orgo Morgo']
more = ['Joe Doe', 'Jane Doe']
names.extend(more)
print(names)  # ['Foo Bar', 'Orgo Morgo', 'Joe Doe', 'Jane Doe']

names = ['Foo Bar', 'Orgo Morgo']
names.append(more)
print(names) # ['Foo Bar', 'Orgo Morgo', ['Joe Doe', 'Jane Doe']]

names = ['Foo', 'Bar']
names.append('Qux')
print(names)   # ['Foo', 'Bar', 'Qux']

names = ['Foo', 'Bar']
names.extend('Qux')
print(names)   # ['Foo', 'Bar', 'Q', 'u', 'x']
