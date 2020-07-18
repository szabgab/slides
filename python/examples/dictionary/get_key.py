user = {
    'fname': 'Foo',
    'lname': 'Bar',
    'address': None,
}

print(user.get('fname'))
print(user.get('address'))
print(user.get('email'))

print(user.get('answer', 42))
