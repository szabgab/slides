from mydate import Date

d = Date(2013, 11, 22)
print(d)

d.set_date(2014, 1, 27)
print(d)
print('')

x = Date.from_str('2013-10-20')
print(x)
print('')

# This works but it is not recommended
z = d.from_str('2012-10-20')
print(d)
print(z)
