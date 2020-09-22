user = {
    'fname': 'Foo',
    'lname': 'Bar',
    'address': None,
}

print(user.get('fname'))
print(user.get('address'))
print(user.get('email'))

print(user.get('answer', 42)) # default returned if key does not exist
print(user.get('address', 23))  # default not returned when key exists but value is None
