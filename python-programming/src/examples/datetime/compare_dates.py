import datetime

t1 = "2013-12-29T11:23:45"
t2 = "2014-01-02T10:19:49"
dt1 = datetime.datetime.strptime(t1, '%Y-%m-%dT%H:%M:%S')
dt2 = datetime.datetime.strptime(t2, '%Y-%m-%dT%H:%M:%S')
dt3 = datetime.datetime.strptime(t2, '%Y-%m-%dT%H:%M:%S')
print(dt1)      # 2013-12-29 11:23:45
print(dt2)      # 2014-01-02 10:19:49

print(dt2 > dt1)   # True
print(dt1 > dt2)   # False
print(dt2 == dt3)  # True
print(dt2 == dt1)  # False

dates = [dt2, dt1, dt3]

print(dates)
# [datetime.datetime(2014, 1, 2, 10, 19, 49), datetime.datetime(2013, 12, 29, 11, 23, 45), datetime.datetime(2014, 1, 2, 10, 19, 49)]
print(sorted(dates))
# [datetime.datetime(2013, 12, 29, 11, 23, 45), datetime.datetime(2014, 1, 2, 10, 19, 49), datetime.datetime(2014, 1, 2, 10, 19, 49)]

