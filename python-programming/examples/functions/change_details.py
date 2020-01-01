a = [5, 6]
b = a        # this is a copy of the *reference* only
             # if we change the list in a, it will
             # change the list connected to b as well
print(a)     # [5, 6]
print(b)     # [5, 6]
a[0] = 1
print(a)     # [1, 6]
print(b)     # [1, 6]


a = {'name' : 'Foo'}
b = a        # this is a copy of the *reference* only
             # if we change the dictionary in a, it will
             # change the dictionary connected to b as well
print(a)     # {'name' : 'Foo'}
print(b)     # {'name' : 'Foo'}
a['name'] = 'Jar Jar'
print(a)     # {'name' : 'Jar Jar'}
print(b)     # {'name' : 'Jar Jar'}

