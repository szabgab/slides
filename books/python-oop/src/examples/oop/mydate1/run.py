from mydate import Date

d = Date(2013, 11, 22)
print(d)

# We can call it on the instance
d.set_date(2014, 1, 27)
print(d)

# If we call it on the class, we need to pass an instance.
# Not what you would normally do.
Date.set_date(d, 2000, 2, 1)
print(d)


# If we call it on the class, we get an error
Date.set_date(1999, 2, 1)
