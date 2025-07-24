import datetime

ts = datetime.datetime.now().replace(
    microsecond=0,
    second=0,
    minute=0,
    hour=0,
)
print(ts)      # 2023-01-19 00:00:00


