# Redis
{id: redis}

## Redis CLI
{id: redis-cli}

[redis-cli](https://redis.io/topics/rediscli)


```
$ redis-cli
> set name foo
> get name
> set name "foo bar"
> get name

> set a 1
> get a
> incr a
> get a

> set b 1
> keys *
> del b
```


## Redis list keys
{id: redis-list-keys}
![](examples/redis/keys.py)


## Redis set get
{id: redis-set-get}
![](examples/redis/set_get.py)


## Redis incr
{id: redis-incr}
![](examples/redis/incr.py)


## Redis incrby
{id: redis-incrby}
![](examples/redis/incrby.py)


## Redis setex
{id: redis-setex}

Set with expiration time in seconds.

![](examples/redis/setex.py)




