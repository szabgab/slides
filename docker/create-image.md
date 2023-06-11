# Create Docker Image Manually
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
docker pull ubuntu:23.04
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
docker run --rm ubuntu:23.04 echo hello
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
docker run -it --name ubu ubuntu:23.04

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

## Rerun (restart) stopped instance
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

* Run container interactively (based on Ubuntu 23.04, call it ubu)

```
docker run -it --name ubu ubuntu:23.04
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
docker history ubuntu:23.04
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


