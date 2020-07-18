user = {
    'fname': 'Foo',
    'lname': 'Bar',
}

for k in user.keys():
    user['email'] = 'foo@bar.com'
    print(k)

print('-----')

for k in user:
    user['birthdate'] = '1991'
    print(k)

# lname
# fname
# -----
# lname
# Traceback (most recent call last):
#   File "examples/dictionary/change_in_loop.py", line 13, in <module>
#     for k in user:
# RuntimeError: dictionary changed size during iteration

