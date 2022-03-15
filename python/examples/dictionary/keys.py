user = {
   'fname': 'Foo',
   'lname': 'Bar',
}

print(user)   # {'lname': 'Bar', 'fname': 'Foo'}

user['email'] = 'foo@bar.com'

print(user.keys())        # dict_keys(['fname', 'lname', 'email'])
print(list(user.keys()))  # ['fname', 'lname', 'email']

