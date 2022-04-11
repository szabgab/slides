user = {
    'fname': 'Foo',
    'lname': 'Bar',
    'answer': None,
}

print('fname' in user)  # True
print('email' in user)  # False
print('answer' in user) # True
print('Foo' in user)    # False

for attr in ['fname', 'email', 'lname']:
    if attr in user:
        print("{} => {}".format(attr, user[attr]))

# fname => Foo
# lname => Bar

