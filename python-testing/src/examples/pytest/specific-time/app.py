import datetime

def daily_task():
    now = datetime.datetime.now()
    print(now)
    if now.month == 1 and now.day == 1:
        return 'new_year'
    if now.month == 2 and now.day == 29:
        return 'leap_day'
    return 'regular'
