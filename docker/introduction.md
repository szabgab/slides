# Docker
{id: docker-intro}

## Why use Docker?
{id: why-use-docker}

{aside}
One of the big problems in software development is the fact that the environment where we develop our code is different from
the environment where QA will test the code that is different from the environment where the application will run in production.
{/aside}

{aside}
This difference can be as simple as having different operating systems, e.g. a developer might use Windows, Linux, or Mac on her desktop
while the production runs on a Linux box. Even if they would use the same operating system, certain dependencies and libraries
installed on these machines might be different. There are various ways to reduce the risk that arises from these differences, one of the
latest and best is the use of some kind of virtualization.
{/aside}

{aside}
Docker is the most popular system to provide virtualization.
{/aside}

* One of the big problems: Developers, Testers, and Production all have different environments.
* Dependency hell.
* On-boarding new developers is hard.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

## What is Docker?
{id: what-is-docker}

{aside}
Docker is usually called a light-weight Virtual Server.

If you are familiar with VirtualBox or VMware you know they allow you to have
a full copy of any operating system running on top of your main operating system. You can even run multiple of these guest operating
systems on a single host operating system. There is full separation and you can install anything on each one of the guests.

However this is very resource intensive as each one of the guest Virtual Servers needs to run its own Operating system taking up a lot
of memory and using a lot of CPU cycles.

Docker also allows to run several guests on the same host, but if the host and the guest are the same type (e.g. both are Linux) then
the guest uses the same kernel as the host and thus requires a lot less additional resources. It has certain limitations such as one service
per each Docker, but these limitations are usually irrelevant in a real-life environment.

The action packaging a whole application inside a Virtual Server is called containerization. There are several solutions to do this, but
Docker got so popular that it is now the de-facto standard.
{/aside}

* A light-weight Virtual Server.

* De-facto standard for containerization.

## Docker container vs. image
{id: docker-container-image}
{i: image}
{i: container}

{aside}
In the world of Docker an **image** is a fixed version of an installed application while a **container** is a running copy of the image.

A Docker image is similar to an ISO image in the world of VirtualBox from which we can create an installation and then run it.
The Docker container in this description would be similar to the already virtual hard-disk a Virtual Server has.


You can download Docker images and you can build your own images based on already existing ones by installing more software on it or copying files to it.
It is frozen on the disk of your host computer.

When you run a Docker **image**, Docker creates a copy of it and we start to call it a **container**. A running instance of the image.
You can still install more applications on a container, but usually it is done only during development time.

Some people also try to use the class-instance analogy to the image-container pair. I am not sure how close is that, but that too is
just an approximation.
{/aside}

container = runtime of an image

* It is like instance = runtime class
* Or Virtual Machine = the running instance of an ISO file.


## Install Docker
{id: install-docker}

{aside}
On modern Linux systems you could use **apt** or **yum** to install Docker, but then you'd get a rather old and outdated version of Docker.
The recommendation of the Docker development team is to download Docker directly from their web-site.

So this is what I recommend as well.

For MS Windows and I think also for Mac, there are two versions. "Docker for Windows" and "Docker for Mac" for the modern
systems. The "Docker Toolbox" for the older versions of MS Windows and Apple Mac, or in case the modern system cannot be installed.

On Linux, you might also need to follow the "Linux post installation instructions".
{/aside}

* Install [Docker](https://www.docker.com/)
* [Get Docker](https://docs.docker.com/get-docker/)

* Linux: Debian/Ubuntu/CentOS: Install the [Docker Engine](https://docs.docker.com/engine/install/)
* MS Windows: Download [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* macOS: Download [Docker for macOS](https://docs.docker.com/docker-for-mac/install/)

* [Post Install for Linux](https://docs.docker.com/install/linux/linux-postinstall/)
* For older Windows and Mac [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)

## Docker on Windows
{id: docker-on-windows}
{i: cmd}

{aside}
The majority of our work with Docker will be on the command line. There probably is some GUI as well, but I have never searched for one
and I have never tried one. In any case I think it is very important that you too, even if you are using MS Windows on your computer
make yourself familiar with the command line instructions of Docker. After all that's how you'll be able to talk to other people
or search for help.

If you are running Docker on top of MS Windows you'll need to open the Command Prompt Window to access the command line of Windows.
So go to Start/Run or click on the "Windows" button on your keyboard and type in "cmd". When you run this application you'll get a black
window where you can type in command.

That's what we are going to use.
{/aside}

* Run the `cmd`


## Docker on Linux and macOS
{id: docker-on-linux}
{i: terminal}

{aside}
On Linux and macOS we are going to us the **terminal** to enter the Docker commands.
{/aside}

* Run the `terminal`

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

Any of the following will show the list of available commands:

```
docker
docker help
docker --help
```

Get help for the various commands on the command-line.

```
docker run --help
docker build --help
```

```
docker help run
docker help build
```

* [docs](https://docs.docker.com/)

## Docker: desktop - host - daemon - client
{id: docker-host-daemon-client}

* Docker desktop A GUI application that helps especially in Windows and macOS
* Docker host (on Windows and macOS it is a Virtual Machine, On Linux it is native).
* Docker daemon runs in the Docker host.
* Docker client runs on the host OS (Linux, Windows macOS).


## Docker Daemon
{id: docker-daemon}

To launch docker daemon from the command line:

* macOS:    `open -a Docker` ot Launch the Docker daemon via the Application icon.
* Linux:     `sudo service docker start`.
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
$ docker container ls -a -s
$ docker ps -as
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES               SIZE
f6239f10a6ad        hello-world         "/hello"            8 seconds ago       Exited (0) 7 seconds ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

* I keep fortgeting what does that `-s` do, so I run:

```
$ docker ps --help
```

There is also an image

```
$ docker images
$ docker image ls
$ docker image list
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
```


## Hello World again
{id: docker-hello-world-again}

This time it will be faster as the images is already on the disk.
A new container is created, ran, and exited.

```
$ docker run hello-world
...

$ docker ps -as

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES               SIZE
42bbb5394617        hello-world         "/hello"            16 minutes ago      Exited (0) 16 minutes ago                       blissful_knuth      0 B (virtual 1.84 kB)
f6239f10a6ad        hello-world         "/hello"            21 minutes ago      Exited (0) 21 minutes ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

## Remove Docker container
{id: docker-remove-container}

```
$ docker rm 42bbb5394617
$ docker container rm blissful_knuth
```

Using the "CONTAINER ID" or the "NAMES" from the list given by ps.

## Remove Docker image
{id: docker-remove-image}

```
$ docker rmi hello-world
$ docker image rm hello-world
```

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
docker container ls
docker container ls -a
docker ps                # list the running containers
docker ps -a             # list all the containers
```

## Remove containers
{id: remove-containers}

```
docker container rm CONTAINER_ID   (or CONTAINER_NAME)
docker rm CONTAINER_ID             (or CONTAINER_NAME)
```

## Remove all the containers with docker prune
{id: docker-prune}
{i: prune}

```
docker container prune
docker container prune -f
docker container prune --force
```

## Remove all Docker containers (old way)
{id: remove-all-docker-containers}
{i: rm}
{i: -aq}

Remove all the docker containers:

```
docker ps -aq
docker rm $(docker ps -aq)
```

## Run and remove container
{id: run-and-remove-container}

```
docker run --rm busybox echo hello world

docker container ls -a      # the container was not left around
```

## Run container mount external disk
{id: run-container-mound-external-disk}


```
docker run --rm "-v%CD%:/opt" -w /opt -it busybox
```

* -w to set the default workdir inside the container
* -v to mount an external folder to an internal folder
* %CD% is the current folder in Windows (outside)
* /opt is the folder inside
* We need double-quotes around it as the currecnt working directory on windows can contain spaces and other special characters.
* --rm to remove the container at the end of the run
* -it interactive mode


## List and remove images
{id: list-and-remove-images}
{i: images}
{i: rmi}

```
docker image ls
docker image rm busybox
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
* Run hello-world
* Run busybox.
* Basically execute all the above commands.
* Check what other interesting command you can find in docker.

