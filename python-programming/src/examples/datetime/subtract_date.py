import datetime

t1 = "2013-12-29T11:23:45"
t2 = "2014-01-02T10:19:49"
dt1 = datetime.datetime.strptime(t1, '%Y-%m-%dT%H:%M:%S')
dt2 = datetime.datetime.strptime(t2, '%Y-%m-%dT%H:%M:%S')
print(dt1)      # 2013-12-29 11:23:45
print(dt2)      # 2014-01-02 10:19:49

diff = dt2-dt1
print(diff)        # 3 days, 22:56:04
print(type(diff))  # <type 'datetime.timedelta'>
print(diff.total_seconds())  # 341764.0

time_travel = dt1-dt2
print(time_travel) #  -4 days, 1:03:56
print(time_travel.total_seconds())  # -341764.0

# d = dt1+dt2
# TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'datetime.datetime'

