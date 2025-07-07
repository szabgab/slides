# Docker Compose PostgreSQL server


In one container start the Docker server, the other one will be the client that is built based on the Dockerfile

{% embed include file="src/examples/postgresql/docker-compose.yml" %}

The Dockerfile is built on top of a plain Ubuntu image

{% embed include file="src/examples/postgresql/Dockerfile" %}

Start the two containers:

```
docker-compose up -d
```

Connect to the client container:

```
$ docker exec -it postgresql_client_1 bash
```


```
# psql -h postgres --username username -d mydb
```

It will ask for a password:

```
Password for user username:
```

type in `password`


```
psql (14.5 (Ubuntu 14.5-0ubuntu0.22.04.1), server 15.1 (Debian 15.1-1.pgdg110+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

mydb=#
```

Alternativel, once inside the client docker container we can put the variable of the database in an environment variable and then we can run a command that will not wait for any input.

```
export PGPASSWORD=password
echo "SELECT CURRENT_TIME" | psql -h postgres -U username mydb
```


