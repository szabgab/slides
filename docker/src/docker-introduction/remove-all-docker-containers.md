# Remove all Docker containers (old way)

* rm
* -aq

Remove all the docker containers:

```
docker ps -aq
docker rm $(docker ps -aq)
```


