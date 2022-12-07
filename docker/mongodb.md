# Docker
{id: docker}

## MongoDB in Docker
{id: mongodb-in-docker}

Start the Docker container

```
docker run -it -d --name mymongo mongo:latest
```

Connect to the Docker container

```
docker exec -it mymongo bash
```

Inside the container start the client and send commands

```
mongosh
db.students.insertOne({"name": "foo", "grades" : { "A" : 1, "B" : 2, "c" : 3, "d" : 4 }});
```
