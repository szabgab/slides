# Create Docker Image
{id: create-docker-image}

## Docker Hub search for images
{id: docker-hub-images}

* Find ready-made images on the [Docker hub](https://hub.docker.com/)

* View the [source of the official images](https://github.com/docker-library/official-images)

## Download image
{id: download-image}

```
docker pull ubuntu:20.04

```

## Use Ubuntu
{id: use-ubuntu}

```
docker run --rm ubuntu:20.04 echo hello
```

```
docker run -it --name ubu ubuntu:20.04

# htop
# apt-get update
# apt-get install htop
# htop
# which perl
# which python
# which python3

# exit
```

## Rerun stopped instance
{id: rerun-stopped-instance}
{i: container}
{i: start}

```
docker container start -i ubu
docker container start -i CONTAINER
```

## Create file in container
{id: create-file-in-container}

```
# echo hello > welcome.txt
# exit
```

Create a file inside the container and then leave the container. It is stopped now again.

## Copy file from stopped container
{id: copy-file-from-stopped-container}
{i: copy}
{i: cp}

```
docker container cp CONTAINER_NAME:FILE .
docker container cp ubu:welcome.txt .
```

On your OS you can copy files from the container to the external filesystem.

## Create your own Docker image
{id: create-your-own-docker-image}

There are two ways to create a Docker image on your computer:

* Run a container, install stuff, stop it, commit it.
* Create Dockerfile, run docker build.

## Create image from container
{id: create-image-from-container}
{i: commit}

```
docker container commit CONTAINER IMAGE
docker container commit ubu mybuntu
```


## Docker: Empty Ubuntu
{id: docker-empty-ubuntu}
{i: FROM}

![](examples/from/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
```

## Docker: Ubuntu Hello World
{id: docker-ubuntu-hello-world}
{i: CMD}

![](examples/hello-world/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
hello world
```

## Docker history
{id: docker-history}

```
docker history IMAGE
```

to see the layers

```
$ docker history ubuntu:20.04
```

![](examples/dock/history_ubuntu.out)


## Docker history - multiple layers
{id: docker-history-multiple-layers}

```
docker history mydocker
```

![](examples/dock/history_mydocker.out)


## Docker: Mounting host directory
{id: docker-mounting-host-directory}

```
$ docker run -it --rm -v /home/gabor/work/slides/docker/examples/python-3:/opt/  mydocker

$ docker run -it --rm -v c:\Users\Gabor Szabo\work\slides\docker\examples python-3:/opt/  mydocker

# cd /opt
# ls -l
```

The `-v HOST:CONTAINER` will mount the `HOST` directory of the home operating system to the `CONTAINER` directory in the Docker container.

```
# ./curl.py -I https://code-maven.com/slides
```

* You can edit the file on your host system (with your IDE) and run it on the command line of the Docker container.


* A better way to mount the current working directory, at least on Linux and OSX

```
docker run -it --rm -v $(pwd):/opt/  mydocker
```


## Distribute command-line script
{id: distribute-command-line-script}


![](examples/python-4/Dockerfile)

```
$ docker build -t mydocker .

$ docker run --rm   mydocker /opt/curl.py https://code-maven.com/slides
```

## Distribute command-line script and include command
{id: distribute-command-line-script-and-include-command}

![](examples/python-5/Dockerfile)


```
$ docker build -t mydocker .


$ docker run --rm   mydocker https://code-maven.com/slides
```


## Docker with crontab
{id: docker-with-crontab}


![](examples/crontab/Dockerfile)

![](examples/crontab/crontab.txt)

```
docker build -t mydocker .
docker run -d --rm --name chronos mydocker

docker container cp chronos:/opt/dates.txt .

docker stop chronos
```

## Exercies 2
{id: exercise-2}

Pick your favorite distribution (Ubuntu, Debian, CentOS, Fedora, etc.) and use it as the base of your application.

* Compile the most recent release of Python from source code (you will need to install some prerequisites).
* Add a Python based application using MongoDB or PostgreSQL or MySQL - whatever you like.
* Prepare it for distribution.

* Install NodeJS, express, create a small web app (hello world would suffice) and prepare it for distribution.

* Create a system of two Flask (or Express) applications that provide APIs and a third command-line application that accesses those APIs.
