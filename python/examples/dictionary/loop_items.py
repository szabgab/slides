user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for tpl in user.items():      # iterates on tuples
    print(f"{tpl[0]} -> {tpl[1]}")
    print("{} -> {}".format(*tpl))

# fname -> Foo
# fname -> Foo
# lname -> Bar
# lname -> Bar
