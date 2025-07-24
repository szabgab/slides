import mydate

dd = mydate.Date.from_str('2013-10-20')
print(dd)

print('')
print(mydate.Date.is_valid_date(2013, 10, 20))
print(mydate.Date.is_valid_date(2013, 10, 32))
print('')

x = mydate.Date.from_str('2013-10-32')

