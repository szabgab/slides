import datetime

ts = "2022-12-20T11:23:45"

# Naive datetime object:
dt = datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S')
now = datetime.datetime.now()
print(now)                      # 2022-12-25 22:39:39.093285
print(dt.tzinfo)                # None
print(now.tzinfo)               # None
elapsed  = now-dt
print(elapsed)                  # 5 days, 11:15:54.093285
print(elapsed.total_seconds())  # 472554.093285
print()

# (Timezone) aware datetime object:
dt_utc = datetime.datetime.strptime(f'{ts}+0000', '%Y-%m-%dT%H:%M:%S%z')
now_utc = datetime.datetime.now(datetime.timezone.utc)
print(now_utc)                     # 2022-12-25 21:39:39.093880+00:00
print(dt_utc.tzinfo)               # UTC
print(now_utc.tzinfo)              # UTC
elapsed_utc  = now_utc-dt_utc
print(elapsed_utc)                 # 5 days, 10:15:54.093880
print(elapsed_utc.total_seconds()) # 468954.09388

