# Docker Compose
{id: docker-compose}

## Install Docker compose
{id: install-docker-compose}

{aside}
Docker compose allows us to configure several docker images to be launched together so they can nicely work together.
For example one image holds the database server, another one holds the message-passing system, and the third holds the application code.

Docker compose can run them all at once and can also define the network connectivity between them.

There are several ways to install Cocker composer. One of them is using pip.
{/aside}

```
pip install docker-compose
```

## Docker compose
{id: docker-compose-0}

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

![](examples/interactive-shell/docker-compose.yml)


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

## Python and Pulsar
{id: python-and-pulsar}

```
docker run -it -p 6650:6650 -p 8080:8080  apachepulsar/pulsar:2.4.1 bin/pulsar standalone
docker build -t mydocker .
docker run --rm -it mydocker bash
```

![](examples/python-pulsar/docker-compose.yml)

![](examples/python-pulsar/Dockerfile)

![](examples/python-pulsar/pulsar_demo.py)

