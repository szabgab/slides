age = 42.12
name = 'Foo Bar'

str_concatenate = "The user " + name + " was born " + str(age) + " years ago."
print(str_concatenate)

str_percentage = "The user %s was born %s years ago." % (name, age)
print(str_percentage)

str_format = "The user {} was born {} years ago.".format(name, age)
print(str_format)

str_f_string = f"The user {name} was born {age} years ago."
print(str_f_string)

