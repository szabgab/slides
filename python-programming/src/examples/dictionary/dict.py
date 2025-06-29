user = {}
user['name'] = 'Foobar'
print(user)        # {'name': 'Foobar'}

user['email'] = 'foo@bar.com'
print(user)        # {'name': 'Foobar', 'email': 'foo@bar.com'}

the_name = user['name']
print(the_name)    # Foobar

field = 'name'
the_value = user[field]
print(the_value)   # Foobar

user['name'] = 'Edith Piaf'
print(user)      # {'name': 'Edith Piaf', 'email': 'foo@bar.com'}
