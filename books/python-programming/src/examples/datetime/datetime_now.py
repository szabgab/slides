import datetime

now  = datetime.datetime.now()
print(now)             # 2015-07-02 16:28:01.762244
print(type(now))       # <type 'datetime.datetime'>

print(now.year)        # 2015
print(now.month)       # 7
print(now.day)         # 2
print(now.hour)        # 16
print(now.minute)      # 28
print(now.second)      # 1
print(now.microsecond) # 762244

print(now.strftime("%Y%m%d-%H%M%S-%f"))  # 20150702-162801-762244
print(now.strftime("%B %b %a %A"))       # July Jul Thu Thursday
print(now.strftime("%c"))                # Thu Jul  2 16:28:01 2015
