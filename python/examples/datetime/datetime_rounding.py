import datetime

now = datetime.datetime.now()
rounded = now - datetime.timedelta(microseconds=now.microsecond)
print(now)     # 2019-11-01 07:11:19.930974
print(rounded) # 2019-11-01 07:11:19

ts = datetime.datetime.now().replace(microsecond=0)

