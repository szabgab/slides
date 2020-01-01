import datetime

usa_date_format   = "%m/%d/%Y" # MM/DD/YYYY
world_date_format = "%d/%m/%Y" # DD/MM/YYYY
other_date_format = "%Y/%m/%d" # YYYY/MM/DD


d = "2012-12-19"
some_day = datetime.datetime.strptime(d, '%Y-%m-%d') # YYYY-MM-DD
print(some_day)         # 2012-12-19
print(type(some_day))   # <type 'datetime.datetime'>

t = "2013-11-04 11:23:45"  # YYYY-MM-DD HH:MM:SS
some_time = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
print(type(some_time))  # <type 'datetime.date'>
print(some_time)        # 2013-11-04
print(some_time.minute) # 23
