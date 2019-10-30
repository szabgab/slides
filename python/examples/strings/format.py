a = 1
b = 'another'

c = "A template with " + str(a) + " and " + b + " value."
print(c)  # A template with 1 and another value.

d = "A template with {} and {} value.".format(a, b)
print(d)  # A template with 1 and another value.
