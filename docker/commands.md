# Commands
{id: commands}

## Dockerfile commands
{id: dockerfile-commands}

{aside}
There is only a handfull of commands that you can use in a Dockerfile. We are going to cover them one-by-one briefly.
{/aside}

* [documentation](https://docs.docker.com/engine/reference/builder/)

* [ADD](docker-add)
* [ARG](docker-arg)
* [CMD](docker-cmd)
* [COPY](docker-copy)
* [FROM](docker-from)
* [ENTRYPOINT](docker-entrypoint)
* [ENV](docker-env)
* [RUN](docker-run)
* [WORKDIR](docker-workdir)

## Docker FROM
{id: docker-from}
{i: FROM}

* Declare the base-image.
* This is how we start all the Dockerfiles. (thought we could put some ARGs before)
* [FROM](https://docs.docker.com/engine/reference/builder/#from)

## Docker COPY
{id: docker-copy}
{i: COPY}

* [COPY](https://docs.docker.com/engine/reference/builder/#copy)
* COPY from host to image

## Docker ARG
{id: docker-arg}
{i: ARG}

* [ARG](https://docs.docker.com/engine/reference/builder/#arg)

## Docker ADD
{id: docker-add}
{i: ADD}

* [ADD](https://docs.docker.com/engine/reference/builder/#add)
* ADD is like COPY but it can do more magic (can download files from the internet, automatically unpacks zipped files)

## Docker RUN
{id: docker-run}
{i: RUN}

* [RUN](https://docs.docker.com/engine/reference/builder/#run)

Execute some command during the creation of the Docker image.

```
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y some-package
```

## Docker CMD
{id: docker-cmd}
{i: CMD}

* [CMD](https://docs.docker.com/engine/reference/builder/#cmd)

CMD - the default command when the container starts

In Debian it is bash.

The CMD only runs when we run the container!

## Docker ENTRYPOINT
{id: docker-entrypoint}
{i: ENTRYPOINT}

* [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint)

## Docker ENV
{id: docker-env}
{i: ENV}

* [ENV](https://docs.docker.com/engine/reference/builder/#env)

## Docker WORKDIR
{id: docker-workdir}
{i: WORKDIR}

* [WORKDIR](https://docs.docker.com/engine/reference/builder/#workdir)

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
## Run container as a daemon - attach detach
{id: run-container-as-a-daemon-attach-detach}
{i: attach}
{i: -d}

* Run as a Daemon in the background name it 'test'

```
docker run -d --rm -it --name test busybox
```

* Check if it is running using `docker ps`

* Attach to it:

```
docker container attach test
```

* Detach from the container and keep it running by pressing

```
Ctrl-p Ctrl-q
```


## Run container as a daemon
{id: run-container-as-a-daemon}
{i: inspect}
{i: logs}

{aside}
In this example we create a Docker image based on busybox and tiny bit of shell command.
Specifically we'll run an infinite while-loop and every second we'll print the current date and time.

The first thing we need to do is to build the 
{/aside}

![](examples/daemon1/Dockerfile)

```
docker build -t mydocker .
docker run -d --rm --name test mydocker
docker inspect test
docker container logs test
docker container attach test
Ctrl-p Ctrl-q
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


