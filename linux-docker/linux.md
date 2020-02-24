# Linux in a Docker Container
{id: linux-in-a-docker-container}

## What is Docker
{id: what-is-docker}

* A light-weight Virtual Server.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.

* De-facto standard for containerization.

## What is Linux
{id: what-is-linux}

* The kernel
* An operating system

## Linux distributions
{id: linux-distributions}

* Debian/Ubuntu
* CentOS/Fedora/RedHat
* [Distrowatch](https://distrowatch.com/)


## Install Docker
{id: install-docker}

Install [Docker](https://www.docker.com/)

* Debian/Ubuntu: `apt-get install docker.io`
* CentOS: `yum install docker`
* MS Windows: Download [Docker Desktop for Windows](https://docs.docker.com/docker-for-windows/install/)
* Mac OSX: Download [Docker for Mac OSX](https://docs.docker.com/docker-for-mac/install/)

* [Post Install](https://docs.docker.com/install/linux/linux-postinstall/)


## Docker on Windows
{id: docker-on-windows}

* cmd

## Docker version
{id: docker-version}

```
docker -v
```

## Docker Run Ubuntu
{id: docker-run-ubuntu}
{i: run}

* Download Ubuntu 19.10 image from [Docker HUB](https://hub.docker.com/)
* Create a container called "ubu" and run it interactively

```
docker run -it --name ubu ubuntu:19.10
```

## Create a footprint on the machine
{id: create-footprint}
{i: ls}
{i: exit}


* list content of the current directory
* create a file
* list the content again
* exit

```
ls -l
echo "Hello World" > GABOR_WAS_HERE
ls -l
exit
```

## Docker restart container
{id: docker-restart}
{i: start}
{i: restart}

```
docker container start -i ubu
ls -l
```

## Docker list containers
{id: docker-list-container}
{i: ps}

```
docker ps -a
```

## Docker remove container
{id: docker-remove-container}
{i: rm}

```
docker rm ubu
```

## Docker list images
{id: docker-list-images}
{i: images}

```
docker images
```

## Docker remove images
{id: docker-remove-images}
{i: rmi}

```
docker rmi ubuntu:19.10
```

## Exercise 1
{id: exercise-1}

* Repeate the above (except that don't remove the image)
* Make sure you have a running system



## Linux File system - directories
{id: linux-file-system-directories}

```
ls
ls -l
ll
alias
cd home
cd ..
cd root
mkdir docs
mkdir docs/text
mkdir documents
mkdir xyz
rmdir xyz
cd dTAB
pwd
```


## Linux File system - files
{id: linux-file-system-files}

```
echo "text" > filename
cat filename
echo "more text" >> filename

nano
```

## Ubuntu Installing packages
{id: ubuntu-installing-package}

```
htop
apt-get update
apt-get install htop
```


## Docker with CentOS
{id: docker-centos}

```
docker run -it --name cent centos:7
yum -y install epel-release
yum install htop
htop
```

## Exercise 2
{id: exercise-2}

* Repeate the above
* In the /root directory create a few subdirectories
* Create a few files with echo, append to the files
* Install nano
* Edit the files


## grep
{id: grep}

```
grep expression filename
```

## find files
{id: find-files}

```
find .
```

## Pipelines
{id: pipelines}

```
find . | grep h
```

