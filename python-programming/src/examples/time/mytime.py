import time

now = time.time()
print(now)             # 1351178170.85
print(type(now))       # <class 'float'>

print(time.timezone)   # -7200 = 2*60*60  (GMT + 2)
print(time.daylight)   # 1 (DST or Daylight Saving Time)

print(time.gmtime())   # time.struct_time
    # time.struct_time(tm_year=2012, tm_mon=10, tm_mday=25,
    # tm_hour=17, tm_min=25, tm_sec=34, tm_wday=3, tm_yday=299, tm_isdst=0)

ts = time.gmtime()
print(ts.tm_year) # 2012

print(time.strftime('%Y-%m-%d %H:%M:%S')) # 2012-10-25 17:16:10

timestamp = 1051178170
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))) # 2003-04-24 12:56:10
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(0)))            # 1970-01-01 00:00:00

