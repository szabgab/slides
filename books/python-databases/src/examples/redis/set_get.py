import redis
r = redis.StrictRedis()

r.set("name", "some value")
print(r.get("name"))

