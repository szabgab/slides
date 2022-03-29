import datetime

date = "2012-12-19"
some_day = datetime.datetime.strptime(date, '%Y-%m-%d') # YYYY-MM-DD
print(type(some_day))   # <type 'datetime.datetime'>
print(some_day)         # 2012-12-19

timestamp = "2013-11-04 11:23:45"  # YYYY-MM-DD HH:MM:SS
some_time = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
print(type(some_time))  # <type 'datetime.date'>
print(some_time)        # 2013-11-04
print(some_time.minute) # 23


# Make sure you know how was the date formatted!

date = "12/3/2012"
dt = datetime.datetime.strptime(date, '%m/%d/%Y') # MM/DD/YYYY date format in USA
print(dt)   # 2012-12-03 00:00:00

dt = datetime.datetime.strptime(date, '%d/%m/%Y') # DD/MM/YYYY date format elsewher
print(dt)   # 2012-03-12 00:00:00

