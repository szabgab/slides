import redis
r = redis.StrictRedis()

r.set("counter", 19) 
print(r.get("counter"))
print(r.incrby("counter", 23))
print(r.get("counter"))


