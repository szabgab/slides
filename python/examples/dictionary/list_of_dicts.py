people = [
    {
        'name'  : 'Foo Bar',
        'email' : 'foo@example.com'
    },
    {
        'name'     : 'Qux Bar',
        'email'    : 'qux@example.com',
        'address'  : 'Borg, Country',
        'children' : [
            'Alpha',
            'Beta'
        ]
    }
]
children = people[1]['children']

print(people)
print(people[0]['name'])
print(people[1]['children'][0])

print(list(map(lambda p: p['name'], people)))

print(children)
children.append("Gamma")
print(children)
print(people)

people[1]['children'] = ['Zorg', 'Buzz']
print()
print(children)
print(people)

