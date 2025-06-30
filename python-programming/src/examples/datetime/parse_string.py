import datetime

dt = datetime.datetime.strptime('Jun 7, 2022', '%b %d, %Y')
print(dt)
print(dt.tzinfo)


dt_utc = datetime.datetime.strptime('Jun 7, 2022 +0000', '%b %d, %Y %z')
print(dt_utc)
print(dt_utc.tzinfo)
