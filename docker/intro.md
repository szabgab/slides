# Docker
{id: index}

## What is Docker?
{id: what-is-docker}

* A light-weight Virtual Server

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

* De-facto standard for containerization

## Docker container vs. image
{id: docker-container-image}

container = runtime image


* It is like instance = runtime class
* Or Virtual Machine = ISO file.


## Install Docker
{id: install-docker}

Install [Docker](https://www.docker.com/)

* Debian/Ubuntu: `apt-get install docker.io`
* CentOS: `yum install docker`
* MS Windows: Download [Docker for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

## Docker version
{id: docker-version}


Show the version of your Docker installation.

```
docker --version

docker version
```

## Docker info
{id: docker-info}

Display some system-wide information.

```
docker info
```

## Docker help on CLI
{id: docker-help-cli}

Get help for the various commands on the command-line.

```
docker --help
docker help run
docker help ps
docker help images
docker help rm
docker help rmi
```

## Docker: host - daemon - client
{id: docker-host-daemon-client}

* Docker host (on Windows and OSX it is a Virtual Machine, On Linux it is native).
* Docker daemon runs in the Docker host.
* Docker client runs on the host OS (Linux, Windows OSX).


## Docker Daemon
{id: docker-daemon}

To launch docker daemon from the command line:

* On OSX:    `open -a Docker` ot Launch the Docker daemon via the Application icon.
* Linux:     `sudo service docker status`
* Windows:    Run the Docker Desktop

## Docker Registry
{id: docker-registry}

* Registry where we store our images.
* Inside a registry there are repositories by user.
* [DockerHub](https://hub.docker.com/)
* Google Cloud [Container registry](https://console.cloud.google.com/gcr/)
* Amazon [AWS Elastic Container Registry](https://aws.amazon.com/ecr/)
* ...

## Docker busybox
{id: docker-busybox}

busybox  (very small)

```
docker run busybox echo hello world

docker run busybox echo something else
```

## Run Interactive
{id: run-interactive}


```
docker run -it busybox

# pwd
# ls -l
# uptime
# echo hello world
```


## Docker List containers
{id: list-containers}

```
docker ps        # running containers
docker ps -a     # all the containers
```

## Remove containers
{id: remove-containers}

```
docker rm CONTAINERID
```

## Remove all Docker containers
{id: remove-all-docker-containers}

Remove all the docker containers:

```
docker ps -aq
docker rm $(docker ps -aq)
```

## Run and remove container
{id: run-and-remove-container}

```
docker run --rm busybox echo hello world

docker ps -a      # the container was not left around
```

## List and remove images
{id: list-and-remove-images}

```
docker images
docker rmi busybox
```


```
docker run -d --rm busybox sleep 30

docker run --name my_name busybox sleep 100

docker inspect CONTAINER_ID
docker logs CONTAINER_ID
```

## Exercise 1
{id: exercise-1}

* Install Docker.
* Run busybox.
* Basically execute all the above commands.
* Check what other interesting command you can find in docker.



## Docker Hub search for images
{id: docker-hub-images}

* [Docker hub](https://hub.docker.com/)

## Download image
{id: download-image}


```
docker pull ubuntu:19.04

```

## Use Ubuntu
{id: use-ubuntu}

```
docker run --rm ubuntu:19.04 echo hello
```

```
docker run -it --rm ubuntu:19.04

# htop
# apt-get update
# apt-get install htop
# htop
# which perl
# which python
# which python3
```

That's really nice, but once we close the container we lose our changes.
When we run again we need to start from scratch.

## Create your own Docker image
{id: create-your-own-docker-image}

There are two ways to create a Docker image on your computer:

* Run a container, install stuff, save it.
* Create Dockerfile, run docker build.

## Docker: Empty Ubuntu
{id: docker-empty-ubuntu}

![](examples/empty/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
```

## Docker: Ubuntu Hello World
{id: docker-ubuntu-hello-world}

![](examples/hello-world/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
hello world
```

## Docker: Perl Hello World
{id: docker-perl-hello-world}

![](examples/hello-world-perl/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello from Perl
```

## Docker: Perl Hello World in script
{id: docker-perl-script-hello-world}

![](examples/hello-world-perl-script/Dockerfile)

![](examples/hello-world-perl-script/hello_world.pl)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello World from Perl script
```

## Docker: Perl with I/O
{id: docker-perl-with-io}

![](examples/perl-io/Dockerfile)

![](examples/perl-io/greetings.pl)

```
$ docker build -t mydocker .
$ docker run --rm mydocker

Use of uninitialized value $name in scalar chomp at /opt/greetings.pl line 7.
Use of uninitialized value $name in concatenation (.) or string at /opt/greetings.pl line 8.
What is your name? Hello , how are you today?
```

We need to tell Docker that this is an interactive process

```
docker run -it --rm mydocker

What is your name? Foo
Hello Foo, how are you today?

```

## Installing Python in Docker
{id: installing-python-in-docker}

![](examples/python-1/Dockerfile)

```
$ docker build -t mydocker .

$ docker run --rm -it mydocker
# which python3
```

## Docker history
{id: docker-history}

```
docker history IMAGE
```

to see the layers

```
$ docker history ubuntu:19.04
IMAGE               CREATED             CREATED BY                                      SIZE
86f1f717b6d8        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B
<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   933B
<missing>           2 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     985kB
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:d3be43e0fdf0de92d…   69MB
```


```
docker history mydocker


IMAGE               CREATED             CREATED BY                                      SIZE
74ffc1660bdd        5 seconds ago       /bin/sh -c apt-get install -y python3           36.8MB
109badc0b51e        14 seconds ago      /bin/sh -c apt-get upgrade -y                   916kB
d7a23dda45d8        18 seconds ago      /bin/sh -c apt-get update                       23.8MB
86f1f717b6d8        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B
<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   933B
<missing>           2 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     985kB
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:d3be43e0fdf0de92d…   69MB
```


## Installing Python in Docker - one layer
{id: installing-python-in-docker-one-layer}

![](examples/python-2/Dockerfile)

```
$ docker build -t mydocker2 .
$ docker history mydocker2

IMAGE               CREATED             CREATED BY                                      SIZE
6158659b63f3        57 seconds ago      /bin/sh -c apt-get update &&     apt-get upg…   60.7MB
86f1f717b6d8        2 weeks ago         /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B
<missing>           2 weeks ago         /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B
<missing>           2 weeks ago         /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   933B
<missing>           2 weeks ago         /bin/sh -c [ -z "$(apt-get indextargets)" ]     985kB
<missing>           2 weeks ago         /bin/sh -c #(nop) ADD file:d3be43e0fdf0de92d…   69MB
```

## Python CLI in Docker
{id: python-cli-in-docker}

![](examples/python-3/curl.py)

![](examples/python-3/Dockerfile)


```
$ docker build -t mydocker .
```

## Docker: Mounting host directory
{id: docker-mounting-host-directory}

```
$ docker run -it --rm -v /home/gabor/work/slides/docker/examples/python-3:/opt/  mydocker

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

## Flask application
{id: flask-application}

![](examples/flask-development/app.py)

![](examples/flask-development/templates/echo.html)

![](examples/flask-development/requirements.txt)


## Flask development
{id: flask-development}

![](examples/flask-development/Dockerfile)

```
$ docker run -it --rm -p:5001:5000 -v $(pwd):/opt/  mydocker

```

Access via [http://localhost:5001/](http://localhost:5001/)


## Docker compose
{id: docker-compose}

```
pip install docker-compose
```

![](examples/flask-redis/docker-compose.yml)
![](examples/flask-redis/Dockerfile)
![](examples/flask-redis/app.py)
![](examples/flask-redis/templates/red.html)
![](examples/flask-redis/requirements.txt)

```
docker-compose up
```

## Docker: Flask + uwsgi
{id: flask-uwsgi}

![](examples/flask-uwsgi/Dockerfile)

![](examples/flask-uwsgi/uwsgi.ini)

## Exercies 2
{id: exercise-2}

Pick your favorite distribution (Ubuntu, Debian, CentOS, Fedora, etc.) and use it as the base of your application.

* Compile the most recent release of Python from source code (you will need to install some prerequisites).
* Add a Python based application using MongoDB or PostgreSQL or MySQL - whatever you like.
* Prepare it for distribution.

* Install NodeJS, express, create a small web app (hello world would suffice) and prepare it for distribution.

* Create a system of two Flask (or Express) applications that provide APIs and a third command-line application that accesses those APIs.


## Dockerfile commands
{id: dockerfile-commands}

* FROM
* COPY
* ADD
* RUN
* CMD
* ENTRYPOINT
* ENV


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


* [Docker Tutorial for Beginners](https://www.youtube.com/watch?v=VlSW-tztsvM)
* [Docker Tutorial For Beginners](https://www.youtube.com/watch?v=sRIxHHZFwBA)


## QA
{id: qa}

* Gabor Szabo https://szabgab.com/
* https://code-maven.com/slides


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

## Docker Perl Dancer hello world app
{id: docker-perl-dancer-hello-world-app}

## Developing Perl code in Docker
{id: developing-perl-code-in-docker}

```
$ docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/hw.pl
```

* Mount a directory of the host OS to a directory in the Docker image.
* Run the code

## Install Perl Modules
{id: install-perl-modules}

Install a perl module using *apt-get*

![](examples/perl-mechanize/Dockerfile)

![](examples/perl-mechanize/get.pl)

```
$ docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl
Usage: /opt/get.pl URL
```

```
docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl http://perlmaven.com/
```

## Links
{id: links}

* [flask uwsgi nginx](https://medium.com/@gabimelo/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e)
* [deploy on Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-go-web-application-with-docker-and-nginx-on-ubuntu-18-04)


