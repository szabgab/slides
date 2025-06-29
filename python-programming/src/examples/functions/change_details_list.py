b = [5, 6]
a = b        # this is a copy of the *reference* only
             # if we change the list in a, it will
             # change the list connected to b as well
print(a)     # [5, 6]
print(b)     # [5, 6]

a[0] = 1
print(a)     # [1, 6]
print(b)     # [1, 6]

a = [7, 8]   # replace the whole list
print(a)     # [7, 8]
print(b)     # [1, 6]

