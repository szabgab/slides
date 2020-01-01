import datetime

d = datetime.datetime.now()
x = d - datetime.timedelta(microseconds=d.microsecond)
print(d) # 2019-11-01 07:11:19.930974
print(x) # 2019-11-01 07:11:19

