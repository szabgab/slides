from mydate import Date

d1 = Date(2013, 11, 22)
print(d1)
print(Date.get_total())
print(Date.total)
print('')

d2 = Date(2014, 11, 22)
print(d2)
print(Date.get_total())
print(Date.total)
print('')

d1.total = 42
print(d1.total)
print(d2.total)
print(Date.get_total())
print(Date.total)

