# Docker Compose
{id: docker-compose}

## Install Docker compose
{id: install-docker-compose}

{aside}
Docker compose allows us to configure several docker images to be launched together so they can nicely work together.
For example one image holds the database server, another one holds the message-passing system, and the third holds the code of the web application.

Docker compose can run them all at once and can also define the network connectivity between them.

There are several ways to install Docker composer. One of them, if you are familiar with Python, is using `pip`.
{/aside}

```
pip install docker-compose
```

## Docker compose
{id: docker-compose-0}
{i: up}
{i: attach}
{i: exec}

{aside}
The configuration of Docker compose is stored in a YAML file, usually called docker-compose.yml.
The following is a very simple example that defines a single Docker container, cleverly named "one"
which is based on the Ubuntu 20.04 image. Normally in order for a Docker container to keep running
you need to execute some command in them that will keep running. We can achieve the same by configuring
the stdin_open and the tty parameters. (They are the same as providing `-it` on the command line of
`docker`.)
{/aside}

![](examples/interactive-shell/docker-compose.yml)

{aside}
In order to launch the Docker containers we need to cd in the directory where we have the docker-compose.yml file and then
type in `docker-compose up`. This will download the image if necessary and launch the Docker container.
{/aside}

```
cd examples/interactive-shell
$ docker-compose up
```

In another terminal, but in the same directory you can run one-of commands on the running container:

```
$ docker exec interactive-shell_one_1 hostname
```

You can also attach to it:

```
$ docker attach interactive-shell_one_1
```

However, when you exit, it will shut down the container.



## Docker compose 1st example
{id: docker-compose-1}

provide command line override for CMD/ENTRYPOINT in the compose yaml file

![](examples/compose1/docker-compose.yml)
![](examples/compose1/Dockerfile)

```
cd examples/compose1
docker-compose up
```

* This builds the image based on the Dockerfile and then launches two containers

## docker compose - keep running two ways
{id: docker-compose-keep-running-two-ways}

![](examples/compose2/docker-compose.yml)
![](examples/compose2/Dockerfile1)
![](examples/compose2/Dockerfile2)

attach to either one of them:

```
docker-compose exec one sh
ping compose1_one_1
```

## Docker Compose
{id: docker-compose-4}

it keeps and reuses the same container unless you remove it with

```
docker-compose rm
```

* [config](https://docs.docker.com/compose/reference/config/)
* [compose-file](https://docs.docker.com/compose/compose-file/)

```
docker-compose up --build

yum install -y net-tools
ifconfig
route -n
ping one
```

![](examples/interactive-shell-two/docker-compose.yml)
![](examples/interactive-shell-two/Dockerfile1)

![](examples/interactive-shell-3/docker-compose.yml)


## Docker Compose Redis server and client
{id: docker-compose-redis-server-and-client}

![](examples/redis/docker-compose.yml)

![](examples/redis/Dockerfile)


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





