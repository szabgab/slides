
def main():
    user = {
        'fname': 'Foo',
        'lname': 'Bar',
    }

    print(user['fname'])
    print(user['email'])

# Foo
# Traceback (most recent call last):
#   File "examples/dictionary/no_such_keys.py", line 9, in <module>
#     print user['email']
# KeyError: 'email'

main()
