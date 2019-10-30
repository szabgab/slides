import redis
import time
r = redis.StrictRedis()


r.setex("login", 2, 'foobar') 
print(r.get("login"))   # 'foobar'
time.sleep(1)
print(r.get("login"))   # 'foobar'
time.sleep(1)
print(r.get("login"))   # None

