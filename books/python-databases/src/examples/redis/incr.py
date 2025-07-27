import redis
r = redis.StrictRedis()

r.set("counter", 40) 
print(r.get("counter"))
print(r.incr("counter"))
print(r.incr("counter"))
print(r.get("counter"))


