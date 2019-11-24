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

print(names)        # <map object at 0x7f2518587780>
print(list(names))  # ['Foo', 'Bar', 'SnowWhite']

