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

* On linux install the [Docker Engine](https://docs.docker.com/engine/install/)
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

{aside}
If we had a full linux system we would have users, and home directories for the users.
We would use the system as one of these users and use either `su` to switch to the root user
or better yet `sudo` to run one-off commands as the `root` user.
{/aside}

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

{aside}
On Linux (actually in the shell we user) there are many commands to deal with the filesystem.
Some of them are listed here.
{/aside}

```
ls
ls -l
ll

alias

pwd

cd home
cd ..
cd root

mkdir docs
mkdir docs/text
mkdir documents
mkdir xyz

rmdir xyz

cd TAB

```

* `ls` list the content of a folder.
* `alias` create aliases for commands so we won't have to type them.
* `pwd` print (current) working directory.
* `cd` change directory
* `mkdir` make directory
* `rmdir` remove directory
* Use TAB completition where possible!


## Linux File system - files
{id: linux-file-system-files}

```
echo Hello World
echo text > filename
cat filename
echo more text >> filename
```

## Ubuntu Installing packages
{id: ubuntu-installing-package}

```
nano
htop
apt-get update
apt-get install nano htop
```

## Docker with CentOS
{id: docker-centos}

```
docker run -it --name cent -w /opt centos:7
```

* To install `nano` type in the following:

```
yum install nano
```

* In order to install `htop` first we need to add EPEL (Extra Packages for Enterprise Linux)

```
yum install epel-release
yum install htop
```

* Then we can use it

```
htop
```

* exit and start again:

```
docker container start -i cent
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
{i: which}

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

```
ll /etc/apt/sources.list
cat /etc/apt/sources.list
grep security /etc/apt/sources.list
grep -v security /etc/apt/sources.list
grep '#' /etc/apt/sources.list
grep '# ' /etc/apt/sources.list
grep '^# ' /etc/apt/sources.list


grep -v '#' /etc/apt/sources.list
grep -v '#' /etc/apt/sources.list | grep security
```


## find files
{id: find-files}

```
find .
find /etc
```

## Pipelines
{id: pipelines}

```
find . | grep h
```

## Create file with bash for loop
{id: create-file-with-bash-for-loop}

```
for i in {0..100}; do echo "Hello $i"; done > /opt/hello
```

## du df
{id: du-df}

```
du
du -h
du -hs

df
df -h
```

## History
{id: history}

```
history
```

## wc - word count
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
{i: printenv}
{i: sort}

```
printenv
printenv | sort
```

## man (manual)
{id: man}

```
man grep
```

