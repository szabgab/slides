# Commands
{id: commands}

## Dockerfile commands
{id: dockerfile-commands}

* FROM
* COPY
* ADD
* RUN
* CMD
* ENTRYPOINT
* ENV
* [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir)


## Docker FROM
{id: docker-from}

* Declare the base-image.
* This is how we start all the Dockerfiles.

## Docker COPY
{id: docker-copy}

COPY from host to image

## Docker ADD
{id: docker-add}

ADD is like COPY but it can do more magic (can download files from the internet, automatically unpacks zipped files)

## Docker RUN
{id: docker-run}

Execute some command during the creation of the Docker image.

```
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y some-package
```

## Docker CMD
{id: docker-cmd}

CMD - the default command when the container starts

In Debian it is bash.

The CMD only runs when we run the container!

## Docker ENTRYPOINT
{id: docker-entrypoint}

## Docker ENV
{id: docker-env}


## Docker upload and publish
{id: docker-upload}

```
docker tag ID szabgab/name:1.01
docker login --username=szabgab
docker push szabgab/name:1.01
```

## Docker upload and publish
{id: docker-ps}

```
docker run --rm -d -it debian
docker ps
docker stop ID

docker exec  0ca23b8a9802 echo hello
docker exec -it 0ca23b8a9802 bash

docker kill ID    if it does not want to stop
```

## Docker Resources
{id: docker-resource}


* [Docker Documentation](https://docs.docker.com/)
* [Docker on Code-Maven](https://code-maven.com/docker)
* [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=VlSW-tztsvM)
* [Docker Tutorial For Beginners](https://www.youtube.com/watch?v=sRIxHHZFwBA)
* [Docker Curriculum](https://docker-curriculum.com/)


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

The command `docker ps -a` shows nothing new.

## Run Docker whale
{id: run-docker-whale}

```
$ docker run docker-whale
```

## Dockerfile
{id: docker-dockerfile}

```
Dockerfile
```

```
FROM debian
RUN apt-get update
RUN apt-get install -y htop
RUN apt-get install -y curl
```

```
docker build -t exp1 .
docker images
docker history exp1
docker run --rm -it exp1
```

## Docker Toolbox
{id: docker-toolbox}

Legacy system

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

no running containers, but there is one on the disk:

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

## Passing command to the Docker Container
{id: passing-commands-to-docker-container}

```
$ docker run mydocker ls -l /

$ docker run mydocker perl -v

This is perl 5, version 22, subversion 2 (v5.22.2) built for x86_64-linux-gnu-thread-multi
....

$ docker run mydocker python -V
container_linux.go:247: starting container process caused "exec: \"python\": executable file not found in $PATH"
docker: Error response from daemon: oci runtime error: container_linux.go:247: starting container process caused "exec: \"python\": executable file not found in $PATH".
ERRO[0001] error getting events from daemon: net/http: request canceled
```

## Links
{id: links}

* [flask uwsgi nginx](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e)
* [deploy on Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker-and-nginx-on-ubuntu-18-04)

## Docker: Flask + uwsgi + nginx
{id: flask-uwsgi-nginx}

Using [https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)

```
docker build -t myapp .
docker run -it --rm -p5001:80 myapp
```

## Run container as a daemon
{id: run-container-as-a-daemon}
{i: inspect}
{i: logs}

```
docker run -d --rm busybox sleep 30

docker run --name my_name busybox sleep 100

docker inspect CONTAINER_ID
docker logs CONTAINER_ID
```

## Inspect low-level information about Docker
{id: inspect-docker-container}
{i: inspect}

```
docker inspect CONTAINER_ID
```

* [inspect](https://docs.docker.com/engine/reference/commandline/inspect/)


## Copy console output of container (logs)
{id: copy-console-of-container}
{i: logs}

```
docker logs CONTAINER_ID
```

* [logs](https://docs.docker.com/engine/reference/commandline/logs/)

## Docker networking
{id: docker-networking}

```
docker network list
NETWORK ID          NAME                DRIVER              SCOPE
234aa213ed9a        bridge              bridge              local
63a0fd629d21        host                host                local
37a165457dad        none                null                local
```

```
docker network create abc      creates a bridge called abc
```

## Ignore files and directories
{id: ignore-files-and-directories}
{i: .dockerignore}

`docker build .`   will send over all the content of the corrent directory to the docker
daemon. You usually don't want that. So add a file called `.dockerignore` to the root
of your project

```
.git/
temp/
```


