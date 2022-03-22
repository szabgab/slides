b = {'name' : 'Foo'}
a = b        # this is a copy of the *reference* only
             # if we change the dictionary in a, it will
             # change the dictionary connected to b as well
print(a)     # {'name' : 'Foo'}
print(b)     # {'name' : 'Foo'}

a['name'] = 'Jar Jar'
print(a)     # {'name' : 'Jar Jar'}
print(b)     # {'name' : 'Jar Jar'}


             # replace reference
a = {'name': 'Foo Bar'}
print(a)     # {'name': 'Foo Bar'}
print(b)     # {'name': 'Jar Jar'}

