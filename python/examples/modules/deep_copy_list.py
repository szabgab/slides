from copy import deepcopy

a = [
    {
      'name': 'Joe',
      'email': 'joe@examples.com',
    },
    {
      'name': 'Mary',
      'email': 'mary@examples.com',
    },
]


b = deepcopy(a)
a[0]['phone'] = '1234'
a[0]['name'] = 'Jane'
a.append({
    'name': 'George'
})

print(a)
print(b)
