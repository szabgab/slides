txt = "Some text"
num = 42.12

print("'{}'".format(txt))     #  as is:   'Some text'
print("'{:12}'".format(txt))  #  left:    'Some text   '
print("'{:<12}'".format(txt)) #  left:    'Some text   '
print("'{:>12}'".format(txt)) #  right:   '   Some text'
print("'{:^12}'".format(txt)) #  center:  ' Some text  '
