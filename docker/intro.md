# Docker
{id: index}

## Install Docker
{id: install-docker}

Install [Docker](https://www.docker.com/)

* Ubuntu: apt-get install docker.io
* CentOS: yum install docker
* Windows: [Docker for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

## Docker help CLI
{id: docker-help-cli}

```
docker --version

docker version

docker --help
docker help run
docker help ps
docker help images
docker help rm
docker help rmi
```

These commands work on the command line even without the daemon, but for anything more serious we need the Docker daemon.

## Docker Daemon
{id: docker-daemon}

On Mac Launch the Docker daemon via the Application icon.


To launch docker daemon from the command line:

* On OSX:    open -a Docker
* Linux:     dockerd    ????
* Windows:   ???

* Docker host (on Windows and OSX it is a Virtual Machine, On linux it is native)
* Docker damon runs in the Docker host
* Docker client runs on the host OS (Linux, Windows OSX)

## docker info
{id: docker-info}

```
docker info
```

## docker container vs. image
{id: docker-container-image}

Container = runtime image

(think about class and instance)


## Docker Registry
{id: docker-registry}

* Registry where we store our images   ([DockerHub](https://hub.docker.com/))
* Inside a registry there are repositories by user.

## Docker busybox
{id: docker-busybox}

busybox  (very small)

```
docker run busybox echo hello world
docker run --rm busybox echo hello world
docker run -d --rm busybox sleep 30

docker run --name my_name busybox sleep 100

docker inspect CONTAINER_ID
docker logs CONTAINER_ID
```

## Docker history
{id: docker-history}

```
docker history IMAGE
```

to see the layers


## Docker create image by save
{id: docker-create-image-by-save}

```
docker run -it debian
apt-get update
apt-get install htop
exit

docker commit 3db0a970e422 USERNAME/debian:1.00
docker run --rm -it USERNAME/debian:1.00
```

Check the history!


## Simple docker commands
{id: simple-docker-commands}

Empty state, no images:

no runnin containers

```
$ docker ps

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

no local containers at all (including not running, and showing the size)

```
$ docker ps -as

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

not even images

```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

Commands

```
docker ps
docker ps -as    list all the containers available locally  (incl the size)
docker images    list images
```

## Docker: Hello World
{id: docker-hello-world}

```
$ docker run hello-world


Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
78445dd45222: Pull complete
Digest: sha256:c5515758d4c5e1e838e9cd307f6c6a0d620b5e07e6f927b07d05f6d12a1ac8d7
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

## After Hello World
{id: docker-after-hello-world}

no running containers, but there is on on the disk:

```
$ docker ps -as
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES               SIZE
f6239f10a6ad        hello-world         "/hello"            8 seconds ago       Exited (0) 7 seconds ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

There is also an image

```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
```

