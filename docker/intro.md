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


## Hello World again
{id: docker-hello-world-again}

This time it will be faster as the images is already on the disk.
A new container is created, ran, and exited.

```
$ docker ps -as

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES               SIZE
42bbb5394617        hello-world         "/hello"            16 minutes ago      Exited (0) 16 minutes ago                       blissful_knuth      0 B (virtual 1.84 kB)
f6239f10a6ad        hello-world         "/hello"            21 minutes ago      Exited (0) 21 minutes ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

## Remove Docker container
{id: docker-remove-container}

```
$ docker rm 42bbb5394617
```

Using the "CONTAINER ID" from the list given by ps.

## Docker Whalesay
{id: docker-hub-whalesay}

Go to [Docker Hub](https://hub.docker.com/) search for *whalesay* and note among the many hits there is one called
[docker/whalesay](https://hub.docker.com/r/docker/whalesay/). We'll use that one.

```
$ docker run docker/whalesay cowsay hello world

Unable to find image 'docker/whalesay:latest' locally
latest: Pulling from docker/whalesay
e190868d63f8: Pull complete
909cd34c6fd7: Pull complete
0b9bfabab7c1: Pull complete
a3ed95caeb02: Pull complete
00bf65475aba: Pull complete
c57b6bcc83e3: Pull complete
8978f6879e2f: Pull complete
8eed3712d2cf: Pull complete
Digest: sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
Status: Downloaded newer image for docker/whalesay:latest
 _____________
&lt; hello world >
 -------------
    \
     \
      \
                    ##        .
              ## ## ##       ==
           ## ## ## ##      ===
       /""""""""""""""""___/ ===
  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~
       \______ o          __/
        \    \        __/
          \____\______/
```

## Docker ps after whalesay
{id: docker-ps-whalesay}

```
$ docker ps -as

CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                      PORTS               NAMES
59c99df0177a        docker/whalesay     "cowsay hello world"   36 minutes ago      Exited (0) 23 minutes ago                       loving_wescoff      0 B (virtual 247 MB)
f6239f10a6ad        hello-world         "/hello"               About an hour ago   Exited (0) 58 minutes ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
docker/whalesay     latest              6b362a9f73eb        21 months ago       247 MB
```

## Docker whale (create Docker image)
{id: docker-whale}

Create *Dockerfile* with the following content:

![](examples/first/Dockerfile)

```
$ docker build -t docker-whale .
...
```

```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
docker-whale        latest              d5cf6bf32c0f        24 seconds ago      277 MB
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
docker/whalesay     latest              6b362a9f73eb        21 months ago       247 MB
```

The command *docker ps -a* shows nothing new.

## Run Docker whale
{id: run-docker-whale}

```
$ docker run docker-whale
```


