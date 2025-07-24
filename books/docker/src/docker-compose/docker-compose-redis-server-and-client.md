# Docker Compose Redis server and client

{% embed include file="src/examples/redis/docker-compose.yml" %}

{% embed include file="src/examples/redis/Dockerfile" %}


Start the docker containers

```
docker-compose up -d
```

Connect to the docker container which has the redis client:

```
docker exec -it redis_client_1 bash
```

Try the following commands in the Docker container:

```
redis-cli -h redis get name
(nil)

redis-cli -h redis set name Foobar
OK


redis-cli -h redis get name
"Foobar"
```

We provide the hostname `redis` because that's the name of the service.
We don't have to provide the port, but if you'd really want to then try this:

```
redis-cli -h redis -p 6379 get name
```



