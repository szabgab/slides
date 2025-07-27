import redis
r = redis.StrictRedis()

for k in r.keys('*'):
    print(k)

