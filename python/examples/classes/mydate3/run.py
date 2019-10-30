from mydate import Date

d = Date(2013, 11, 22)
print(d)

print('')
dd = Date.from_str('2013-10-20')
print(dd)

print('')
print(Date.get_total())
print(Date.total)

