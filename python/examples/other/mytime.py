import time

print(time.time())     # 1351178170.85

print(time.timezone)   # 7200 = 2*60*60  (GMT + 2)
print(time.daylight)   # 1 (DST or Daylight Saving Time)

print(time.gmtime())   # time.struct_time
    # time.struct_time(tm_year=2012, tm_mon=10, tm_mday=25,
    # tm_hour=17, tm_min=25, tm_sec=34, tm_wday=3, tm_yday=299, tm_isdst=0)

t = time.gmtime()
print(t.tm_year) # 2012

print(time.strftime('%Y-%m-%d %H:%M:%S')) # with optional timestamp

