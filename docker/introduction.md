# Docker
{id: docker-intro}

## Why use Docker?
{id: why-use-docker}

{aside}
One of the big problems in software development is the fact that the environment where we develop our code is different from
the environment where QA will test the code that is different from the environment where the application will run in production.
{/aside}

{aside}
This difference can be as simple as having different operating systems, e.g. a developer might use Windows or Linux on her desktop
while the production runs on a Linux box. Even if they would use the same operating system, certain dependencies and libraries
installed on these machines might be different. There are various ways to reduce the risk that arises from these difference, one of the
latest and best is the use of some kind of virtualization.
{/aside}

{aside}
Docker is the most popular system to provide virtualization.
{/aside}

* One of the big problems: Developers, Testers, and Production all have different environments.
* Dependency hell.
* Onboarding new developers is hard.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

## What is Docker?
{id: what-is-docker}

* A light-weight Virtual Server.

* De-facto standard for containerization.

## Docker container vs. image
{id: docker-container-image}
{i: image}
{i: container}

{aside}
In the world of Docker an **image** is similar to an iso image in the world of VirtualBox.
When we run an image Docker creates a copy of it and it is now called a **container**.
A running instance of the image.
{/aside}

container = runtime image


* It is like instance = runtime class
* Or Virtual Machine = the running instance of an ISO file.


## Install Docker
{id: install-docker}

Install [Docker](https://www.docker.com/)

* [Get Docker](https://docs.docker.com/get-docker/)

* Debian/Ubuntu: `apt-get install docker.io`
* CentOS: `yum install docker`
* MS Windows: Download [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* Mac OSX: Download [Docker for Mac OSX](https://docs.docker.com/docker-for-mac/install/)

* [Post Install for Linux](https://docs.docker.com/install/linux/linux-postinstall/)
* For older Windows and Mac [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

## Docker on Windows
{id: docker-on-windows}
{i: cmd}

* Run the `cmd`


## Docker --version
{id: docker--version}
{i: --version}

Show the version of your Docker installation.

```
docker --version
```

Output:

```
Docker version 19.03.6, build 369ce74a3c
```

## Docker version
{id: docker-version}
{i: version}


Show a lot more details about Docker:

```
docker version
```

Output:

```
Client:
 Version:           19.03.6
 API version:       1.40
 Go version:        go1.12.10
 Git commit:        369ce74a3c
 Built:             Fri Feb 28 23:26:00 2020
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          19.03.6
  API version:      1.40 (minimum version 1.12)
  Go version:       go1.12.10
  Git commit:       369ce74a3c
  Built:            Wed Feb 19 01:04:38 2020
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.3.3-0ubuntu1~19.10.1
  GitCommit:
 runc:
  Version:          spec: 1.0.1-dev
  GitCommit:
 docker-init:
  Version:          0.18.0
  GitCommit:

```

## Docker info
{id: docker-info}
{i: info}

Display some system-wide information.

```
docker info
```

## Docker help on CLI
{id: docker-help-cli}
{i: help}

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
* Linux:     `sudo service docker status`.
* Windows:    Run the Docker Desktop.

## Docker Registry
{id: docker-registry}

{aside}
A Docker registry is a place where we can store reusable Docker images. There are several public or semi-publick Docker Registries and you can also
run your own private registry in your organization. The most well known registry is maintained by Docker itself.
The major cloud providers run their own registries tightly integrated with their other cloud services.
{/aside}

* Registry where we store our images.
* Inside a registry there are repositories by user.
* [DockerHub](https://hub.docker.com/). Free hosting of public images. Paid hosting of private images.
* Google Cloud [Container registry](https://console.cloud.google.com/gcr/).
* Amazon [AWS Elastic Container Registry](https://aws.amazon.com/ecr/).
* ...
* [Deploy your own registry](https://docs.docker.com/registry/deploying/).


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


## Docker busybox
{id: docker-busybox}
{i: busybox}
{i: run}

{aside}
**busybox** is a very small image with some essential Linux tools.
{/aside}

```
docker run busybox echo hello world

docker run busybox echo something else
```

## Run Interactive
{id: run-interactive}
{i: -it}


```
docker run -it busybox

# pwd
# ls -l
# uptime
# echo hello world
```


## Docker List containers
{id: list-containers}
{i: ps}

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
{i: rm}
{i: -aq}

Remove all the docker containers:

```
docker ps -aq
docker rm $(docker ps -aq)
```

## Remove all the containers with docker prune
{id: docker-prune}
{i: prune}

```
docker container prune
docker container prune -f
```

## Run and remove container
{id: run-and-remove-container}

```
docker run --rm busybox echo hello world

docker ps -a      # the container was not left around
```

## List and remove images
{id: list-and-remove-images}
{i: images}
{i: rmi}

```
docker images
docker rmi busybox
```

## Docker remove all the images - prune images
{id: remove-all-the-images}

```
docker image prune
docker image prune -a
docker image prune -a -f
```

## Exercise 1
{id: exercise-1}

* Install Docker.
* Run busybox.
* Basically execute all the above commands.
* Check what other interesting command you can find in docker.


