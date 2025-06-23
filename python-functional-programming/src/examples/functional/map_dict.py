people = [
    {
        'name': 'Foo',
        'phone': '123',
    },
    {
        'name': 'Bar',
        'phone': '456',
    },
    {
        'name': 'SnowWhite',
        'phone': '7-dwarfs',
    }
]

names = map(lambda d: d['name'], people)

print(names)
print(list(names))
