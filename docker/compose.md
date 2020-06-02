# Docker Compose
{id: docker-compose}

## Docker compose 1
{id: docker-compose-1}

provide command line override for CMD/ENTRYPOINT in the compose yaml file

![](examples/compose1/docker-compose.yml)
![](examples/compose1/Dockerfile)

## docker compose - keep running two ways
{id: docker-compose-keep-running-two-ways}

![](examples/compose2/docker-compose.yml)
![](examples/compose2/Dockerfile1)
![](examples/compose2/Dockerfile2)

attach to either one of them:

```
docker-compose exec one sh
```

## Docker compose
{id: docker-compose-0}

```
$ docker-compose u
$ docker attach net_one_1
$ docker-compose exec one sh
```

![](examples/interactive-shell/docker-compose.yml)

## Docker Compose
{id: docker-compose-4}

it keeps and reuses the same container unless you remove it with

docker-compose rm
https://docs.docker.com/compose/reference/config/
https://docs.docker.com/compose/compose-file/

docker-compose up --build

yum install -y net-tools
ifconfig
route -n
ping one


![](examples/interactive-shell-two/docker-compose.yml)
![](examples/interactive-shell-two/Dockerfile1)

![](examples/interactive-shell-3/docker-compose.yml)

## Flask with Redis
{id: flask-with-redis}

![](examples/flask-redis/app.py)
![](examples/flask-redis/templates/red.html)
![](examples/flask-redis/requirements.txt)


## Docker compose
{id: docker-compose-redis-flask}

```
pip install docker-compose
```

![](examples/flask-redis/docker-compose.yml)
![](examples/flask-redis/Dockerfile)

```
docker-compose up
```


