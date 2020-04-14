# Docker
{id: docker-intro}

## What is Docker?
{id: what-is-docker}

* A light-weight Virtual Server.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

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

* Registry where we store our images.
* Inside a registry there are repositories by user.
* [DockerHub](https://hub.docker.com/). Free hosting of public images. Paid hosting of private images.
* Google Cloud [Container registry](https://console.cloud.google.com/gcr/).
* Amazon [AWS Elastic Container Registry](https://aws.amazon.com/ecr/).
* ...
* [Deploy your own registry](https://docs.docker.com/registry/deploying/).

## Docker busybox
{id: docker-busybox}
{i: busybox}
{i: run}

busybox  (very small)

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

## Exercise 1
{id: exercise-1}

* Install Docker.
* Run busybox.
* Basically execute all the above commands.
* Check what other interesting command you can find in docker.

## Docker remove all the images - prune images
{id: remove-all-the-images}

```
docker image prune
docker image prune -a
docker image prune -a -f
```
