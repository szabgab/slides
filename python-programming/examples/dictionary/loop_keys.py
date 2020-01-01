user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for k in user.keys():
    print(k)

# lname
# fname

for k in user.keys():
    print("{} -> {}".format(k, user[k]))

# lname -> Bar
# fname -> Foo
