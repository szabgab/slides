people = [
    {
        'name'  : 'Foo Bar',
        'email' : 'foo@example.com'
    },
    {
        'name'     : 'Tal Bar',
        'email'    : 'tal@example.com',
        'address'  : 'Borg, Country',
        'children' : [
            'Alpha',
            'Beta'
        ]
    }
]
children = people[1]['children']

# print(people)
print(people[0]['name'])
print(people[1]['children'][0])
people[1]['children'].append('Gamma')
print(children)

print(list(map(lambda p: p['name'], people)))

people[0]['children'] = ['Zorg', 'Buzz']

