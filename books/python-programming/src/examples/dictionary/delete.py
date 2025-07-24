user = {
    'fname': 'Foo',
    'lname': 'Bar',
    'email': 'foo@bar.com',
}

print(user) # {'lname': 'Bar', 'email': 'foo@bar.com', 'fname': 'Foo'}

fname = user['fname']
del user['fname']
print(fname) # Foo
print(user) # {'lname': 'Bar', 'email': 'foo@bar.com'}

lname_was = user.pop('lname')
print(lname_was) # Bar
print(user) # {'email': 'foo@bar.com'}

