# Create Docker Image
{id: create-docker-image}

## Create your own Docker image
{id: create-your-own-docker-image}

{aside}
There are two ways to create a Docker image on your computer:
{/aside}

* Run a container, install stuff, stop it, commit it.
* Create Dockerfile, run docker build.

{aside}
We will do both, but we start with the first one.
It is less common, but it is more fun and it is easier to understand.

Besides while you are researching a topic you will follow the path of the first
technique, only when you found the way to accomplish some task will you formalize it in a Dockerfile.
{/aside}


## Docker Hub search for images
{id: docker-hub-images}

{aside}
Before we start creating our own Docker images, let's take a moment exploring what images already exist?
After all our goal is to solve problems not just to create random Docker images, so if there is already one that serves our purposes
then it is better to use that.

Moreover, every Docker image we are going to build is going to be based on an already existing image.

If you visit the Docker hub and start searching you'll see there are tons of low-level images that provide the
basics of one of the Linux distributions. For example, search for **Ubuntu** and you'll see there is an official Ubuntu
image.

There are also application level images, for example there are imagaes for **Wordpress** and there are images that already include
a certain Database (e.g. PostgreSQL) and other images that contain a programming language. For example **Python**.

In addition you can find the source of all the official images in A GitHub repository.
Once you get familiar with the basics of Docker, it might be useful to review them.
{/aside}

* Find ready-made images on the [Docker hub](https://hub.docker.com/)

* View the [source of the official images](https://github.com/docker-library/official-images)

## Download image
{id: download-image}
{i: pull}

{aside}
Earlier when we used the `run` command to run a Docker images, the first thing it did was downloading the image.
Subsequent `run` commands only executed the image.

You could actully download images without running them using the `pull` command. You only need to provide the name and the tag
of the image.
{/aside}

```
docker pull ubuntu:20.04
```

## Use Ubuntu to run a single command
{id: use-ubuntu}

{aside}
As earlier we saw how to use the **busybox** image, but most people are not familiar with busybox, so let's see a few examples
using the Ubuntu image. We are still not building our own image at this point, just playing with a ready-made image.

The `run` command allows us to launch a Docker container based on an image. The `--rm` flag tells Docker to remove the container from
ou harddisk once it stopped running. It is a good idea to do so if you don't need the conatainer any more. Otherwise the dead containers
would just accumulate and take up disk space.

After the name of the image we can also provide the command line that needs to be execute. In this case `echo hello` is just a simple shell command.

Running this will print `hello` and then the conatiner will exit and it will be removed from the disk as if it never existed.
{/aside}

```
docker run --rm ubuntu:20.04 echo hello
```

## Use Ubuntu interactively
{id: use-ubuntu-interaqctively}

{aside}
The next best thing we can do is to launch our Docker container in an interactive mode.
This time we proved the `-i` and `-t` flags together as `-it` to allow for interactive mode.
We don't use the `--rm` flag as we'll want the container to stay even after we exit,
so we can re-launch the same container.

By default Docker will give a name to each container consisteing two random names, eg. `foo_bar`,
but that makes it harder for use to re-launch the container. So in this case we used the `--name`
flag to give it a name. The brilliant name I selected was `ubu`.

Once we execute the command we will see the prompt as it is displayed by the container.
Now we can execute various Linux command. For example we can try to tun `htop`.

If you try to do this you'll quickly find out that this image did not come with the `htop` command.
Don't worry though we can easily install it. We run the `apt-get update` command to download the list
of all the available packages. (We don't need to use `sudo` as we are running as user `root` inside
the Docker container.)

Once we downloaded the up-to-date list of packages, we can run `apt-get install htop` to download and install
the `htop` pacakge and then we can try to use it.

At this point feel free to play around with the command line. For example use the `which` command to check
if certain programs or certain programming languages were installed.

Once you had enough you can press `Ctrl-D` or type in `exit` to leave the container.
Once you leave it the container stops running.  You can then use the `docker ps -a` command to see
the exited Docker container called ubu.
{/aside}

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

```
docker ps -a
```

## Rerun stopped instance
{id: rerun-stopped-instance}
{i: container}
{i: start}

{aside}
It is great that we have a container on the disk which is not runnin any more, but what can we do with it?

Probably the most important thing is that we can re-launch it. Type in `docker container start -i ubu` and
you'll be back inside the same container. How do you know it is the same?  You can run `htop` and see it is installed.
If you were running a new container you'd have no `htop` installed as that's not part of the Ubuntu image as
it was downloaded from the Docker hub.
{/aside}


```
docker container start -i ubu
docker container start -i CONTAINER
```

## Create file in container
{id: create-file-in-container}

{aside}
Let's do another small experiment. If you have left it again, let's get back to the ubu container by running
`docker container start -i ubu` and then let's create a file. Nothing major, just a file called `welomce.txt`
with the content "hello" in it. (You can use the `echo` command with redirection to accomplish this.

Then type in `exit` to leave the container and to let it stop. You alread know how to list all the containers
so you can verify it still exists but it does not run any more.
{/aside}

```
# echo hello > welcome.txt
# exit
```

* Create a file inside the container and then leave the container. It is stopped now again.

## Copy file from stopped container
{id: copy-file-from-stopped-container}
{i: copy}
{i: cp}

{aside}
At this point we could get back to the container and verify that the file is still there, and I encourage you do that,
but we would like to do something else as well. We would like to be able to see the file even though the container
does not run any more. We can do this by running the `docker container cp` command.

The command gets two parameters, the first one contains the name of the container and the path to the file
inside the container we would like to copy. The second parameter is the name or location of the file outside
the container. dot `.` just means, copy the file here with the same name as we had inside.

The `cp` command looks similar to the `cp` command of Linux.
{/aside}

```
docker container cp CONTAINER_NAME:FILE .
docker container cp ubu:welcome.txt .
```

* On your host OS you can copy files from the container to the external filesystem.

## Create image from container
{id: create-image-from-container}
{i: commit}

{aside}
Now that we have a conatainer with all the necessary packages installed (htop)
and all the necessary files created (welcome.txt) let's convert this container
into an image. Let's freeze this container so it will become reusable.
Either by me or by others as well.

We can do this by running the `docker container commit` command. It needss to get
the name of the contain as the base-container and the name and tag of the
new image. Here I used the name "myubu"

Once we have the new image we can list it using the `docker images` command and we can
run it with the regular `run` command.
{/aside}

```
docker container commit CONTAINER IMAGE
docker container commit ubu myubu:1.00
```

```
docker images
docker container run --rm -it myubu:1.00
```

## Docker create image manually
{id: docker-create-image-manually}

{aside}
We went over this step-by-step earlier, but let's have all the step in one place:
{/aside}

* Run container interactively (based on Ubuntu 20.04, call it ubu)

```
docker run -it --name ubu ubuntu:20.04
```

* Install packages, copy or create files, etc..., exit.

```
# apt-get update
# apt-get install htop
# echo "Hello World" > welcome.txt
# exit
```

* Create the image called myubu from the container called ubu

```
docker container commit ubu myubu:1.00
```

* Run a container based on the new image called myubu:

```
docker container run --rm -it myubu:1.00
```


## Check the history!
{id: check-docker-history}

```
docker history ubuntu:20.04
docker history myubu:1.00
```

## Docker create image manually - placeholders
{id: docker-create-image-manually-placeholder}

* Run conatiner

```
docker run -it --name NAME BASE_CONTAINER:BASE_TAG
```

* install stuff in the container, copy stuff to the container, exit

* Create image from container

```
docker container commit CONTAINER NEW_IMAGE_NAME:TAG
```

* Better yet, create the container under your Docker Hub username:

```
docker container commit CONTAINER USERNAME/NEW_IMAGE_NAME:TAG
```

* To verify, run a container based on the new image (with or without username):

```
docker container run --rm -it NEW_IMAGE_NAME:TAG
docker container run --rm -it USERNAME/NEW_IMAGE_NAME:TAG
```

## Docker: Empty Ubuntu
{id: docker-empty-ubuntu}
{i: FROM}

{aside}
Creating new Docker images manually, as we saw earlier, is fun as you can experiment a lot and you get immediate feedback
as you intsall more things in the running container. However this is not easily reproducible. For one thing it happens to
me a lot that I install a package and later I find out I probbaly don't need it.

Once you have a good grasp on what do you really need in that image, you can create a set of instructions in
a Dockerfile that will create the image for you.

There are many advantages to this approach.

* You get an instant description of what is really in the image.
* It can be reproducible, so you or someone else can later rebuild the same image.
* As it is a plain text file you can put it in version control and track the changes.
* It is very small, compared to the size of the image.

In this very first example we will create a new image that is based on and is identical to the Ubuntu 20.04 image.
Without any extra.

For this we create a new directroy and in that directory we create a file called `Dockerfile` and with a single line in it: `FROM ubutu:20.04`.
Every Dockerfile must declare the image it is based on. We don't have any more commands in the Dockerfile so we don't add anything to
this image.

cd into the directory where we have this file and run `docker build -t mydocker .` (The dot at the end of the command is important.)

This will create an image called `mydocker` using the `Dockerfile` in the current directory and using all the context of this directory (indicated by the dot).
We'll discuss the "context" in a bit, for now it only contains the Dockerfile. That's why we created this in a new empty directory.

Once the image is created we can use it exactly as we used the original Ubuntu image.
{/aside}

![](examples/from/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
```

## Docker: Ubuntu Hello World
{id: docker-ubuntu-hello-world}
{i: CMD}

{aside}
Having an image identical to some already existing image does not give us a lot of value, so let's create make another small step.
Let's add another instruction to the Dockerfile called `CMD`. The content of the `CMD` line is not executed when we build the image.
Whatever comes after this `CMD` will be executed when we start the Docker container based on this image. Unless we override it.

In our case we just use the shell command `echo` to print "hello world" to the screen.
{/aside}

![](examples/hello-world/Dockerfile)

```
$ docker build -t mydocker .
```

{aside}
Once the image is ready we can run it and it will print out "hello world" as expected. You could distribute this image to show that you made it!
Well, we have not seen yet how to distribute the image, but aside of that everything is fine.
{/aside}

```
$ docker run --rm mydocker
hello world
```

{aside}
The user of this new image can provide her own command on the command line, either another echo command or something
totally different such as the `pwd` below.
{/aside}

```
docker run --rm mydocker echo Other text
Other text
```

```
docker run --rm mydocker pwd
/
```

If we try to run it in interactive mode by supplying the `-it` flags, we'll find out that Docker still runs or `CMD` and exits.
In order to really get into the interactive shell of this container we need to override the default `CMD` by a call to `bash`.

```
docker run -it --rm mydocker bash
```

## Docker curl
{id: docker-curl}

{aside}
In the previous example we saw that we can use commands other than `echo`, but what if we would like to use `curl` for example?
It will fail because `curl` is not installed in the image.
{/aside}

```
$ docker run  --rm mydocker curl https://code-maven.com/
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \"curl\": executable file not found in $PATH": unknown.
```

{aside}
To install it we need to add `RUN` commands. (Yeah, I know the name might be a bit confusing, but think about it from the point of view of the build process.
We would like to run something during the build process.)

In order to install the `curl` package in Ubuntu we need to execute the `apt-get install -y curl` command.
(The `-y` flag is there so `apt-get` will not ask for confirmation.)
However before we can execute that command we need to download the list of all the available packages. We do that by running (here is that word!)
the `apt-get update` command.

We don't have a `CMD` as we don't have a default operation.
{/aside}

![](examples/curl/Dockerfile)

{aside}
We can build the image the same way we built the previous one.
{/aside}

```
$ docker build -t mydocker .
```

{aside}
Then we can run it. This time it will execute the `curl` command.
{/aside}

```
$ docker run  --rm mydocker curl https://code-maven.com/
```


## Docker history
{id: docker-history}

{aside}
Each Docker images is built by layers upon layers.

The `docker history` command can show you these layers.

Here you can see that the Ubuntu image we have downloaded from the Docker Hub has 5 layers.
{/aside}

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
