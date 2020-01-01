a = {
    'name': 'Foo Bar',
    'grades': {
       'math': 70,
       'art' : 100,
    },
    'friends': ['Mary', 'John', 'Jane', 'George'],
}

b = a
a['grades']['math'] = 90
a['email'] = 'foo@bar.com'
print(a)
print(b)

