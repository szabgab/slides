user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for key in user.keys():
    print(key)

# lname
# fname

for key in user.keys():
    print(f"{key} -> {user[key]}")

# lname -> Bar
# fname -> Foo
