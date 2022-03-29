import datetime

t1 = "2013-12-29T11:23:45"
t2 = "2014-01-02T10:19:49"
dt1 = datetime.datetime.strptime(t1, '%Y-%m-%dT%H:%M:%S')
dt2 = datetime.datetime.strptime(t2, '%Y-%m-%dT%H:%M:%S')
dt3 = datetime.datetime.strptime(t2, '%Y-%m-%dT%H:%M:%S')
print(dt1)      # 2013-12-29 11:23:45
print(dt2)      # 2014-01-02 10:19:49

d = dt2-dt1
print(d)        # 3 days, 22:56:04
print(type(d))  # <type 'datetime.timedelta'>
print(d.total_seconds())  # 341764.0

print(dt2 > dt1)   # True
print(dt1 > dt2)   # False
print(dt2 == dt3)  # True
print(dt2 == dt1)  # False

nd = dt1 + datetime.timedelta(days = 3)
print(nd)       # 2014-01-01 11:23:45
