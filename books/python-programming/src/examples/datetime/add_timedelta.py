import datetime

timestamp = "2013-12-29T11:23:45"
ts = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')
print(type(ts))
diff = datetime.timedelta(days = 3)
print(diff)
nts = ts + diff
print(type(nts))
print(ts)
print(nts)       # 2014-01-01 11:23:45
