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

* [Docker](https://www.docker.com/)

* Un linux install the [Docker Engine](https://docs.docker.com/engine/install/)
* MS Windows: Download [Docker Desktop for Windows](https://docs.docker.com/engine/install/)
* macOS: Download [Docker Desktop for macOS](https://docs.docker.com/engine/install/)

* [Post Install for Linux](https://docs.docker.com/install/linux/linux-postinstall/)

* For older Windows and Mac there was something called Docker Toolbox. But now only [this](https://docs.docker.com/desktop/)

## Docker on Windows
{id: docker-on-windows}

* Run the `cmd`

## Docker version
{id: docker-version}

```
docker -v
```

## Docker Run Ubuntu
{id: docker-run-ubuntu}
{i: run}

* [Download Ubuntu image](https://hub.docker.com/_/ubuntu) from [Docker HUB](https://hub.docker.com/)
* Create a container called "ubu" and run it interactively

```
docker run -it -w /opt --name ubu ubuntu:22.10
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

* As we can see the file is still there.

## Docker list running containers
{id: docker-list-running-container}
{i: ps}

* In another terminal/command window:

```
docker ps
```

## Docker list all containers
{id: docker-list-container}
{i: ps}

* Exit from the container

```
docker ps -a
```


## Docker list images
{id: docker-list-images}
{i: images}

```
docker images
docker image list
docker image ls
```

## Docker remove images
{id: docker-remove-images}
{i: rmi}

```
docker rmi ubuntu:22.10
docker image rm ubuntu:22.10
```

* This will fail as the container is still referencing it

## Docker remove container
{id: docker-remove-container}
{i: rm}

```
docker container rm ubu
```

## Exercise 1
{id: exercise-1}

* Repeate the above (except that don't remove the image)
* Make sure you have a running system

## root
{id: root}

* Several meanings:

* The name of the superuser or administrator: `root`
* The name we use for the common ancestor of the filesystem: `/`
* The name of the home-directory of user 'root': `/root`
* `/opt` is usually where people put all kinds of optional installations

## Linux Users
{id: linux-users}

* users (root and other users)
* /home directory
* su
* sudo

```
ls /root
ls /home/
```

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

* Create a new alias

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

## Bashrc
{id: bashrc}

* The configuration file of our shell

```
/root/.bashrc
~/.bashrc
```

* Configure a new alias


## Exercise 2
{id: exercise-2}

* Repeate the above
* In the /root directory create a few subdirectories
* Create a few files with echo, append to the files
* Install nano
* Edit the files
* Create a new alias for the current shell (eg. lx to do something)
* Add it to the .bashrc and check if it is persistant

## which type
{id: which-type}

```
which ls
which python
which ll
type ll
```

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

## du df
{id: du-df}

```
du -h
df -h
```

## History
{id: history}

```
history
```

## wc
{id: wc}

```
wc
```

## clear screen
{id: clear}

```
clear
Ctrl-L
```

## printenv
{id: printenv}

```
printenv
```

