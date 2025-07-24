user = {
    'fname': 'Foo',
    'lname': 'Bar',
    'address': None,
}

print(user.get('fname'))        # Foo     - because 'fname' has the value 'Foo'
print(user.get('email'))        # None    - because 'email' does not exist
print(user.get('address'))      # None    - because 'address' has the value None

# set a default value to return
print(user.get('fname', 'ABC')) # Foo     - because the value of 'fname' is 'Foo'
print(user.get('answer', 42))   # 42      - because 'answer' does not exist
print(user.get('address', 23))  # None    - because None is the value of the 'address' key
