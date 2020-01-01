user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for t in user.items():      #  returns tuples
    print("{} -> {}".format(t[0], t[1]))
    #print("{} -> {}".format(*t))

# lname -> Bar
# fname -> Foo
