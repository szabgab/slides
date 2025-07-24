# Docker Compose MongoDB server


In one container start the Docker server, the other one will be the client that is built based on the Dockerfile

{% embed include file="src/examples/mongodb/docker-compose.yml" %}

The Dockerfile is also based on the official mongodb image as that made it easy to have `mongosh` already installed.

{% embed include file="src/examples/mongodb/Dockerfile" %}

Start the two containers:

```
docker-compose up -d
```

Connect to the client container:

```
docker exec -it mongodb_client_1 bash
```

Start the mongodb client and connect to the server running in the other container

```
mongosh mongodb://mongodb:27017
```


