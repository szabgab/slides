# Dockerfile
{id: dockerfile}

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

In this very first example we will create a new image that is based on and is identical to the Ubuntu 23.04 image.
Without any extra.

For this we create a new directroy and in that directory we create a file called `Dockerfile` and with a single line in it: `FROM ubutu:23.04`.
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

## Docker: Ubuntu htop
{id: docker-ubuntu-htop}
{i: RUN}

{aside}
Previously we created a Docker image manually after we have installed `htop` and created a file manually in a Docker container.
Let's do the same now using Dockerfile.
{/aside}

![](examples/ubuntu-htop/Dockerfile)

```
docker build -t mydocker .
docker run --rm -it mydocker
```

## Docker COPY welcome file
{id: docker-copy-welcome-file}
{i: COPY}

![](examples/ubuntu-copy-welcome/Dockerfile)

```
docker build -t mydocker .
docker run --rm -it mydocker
```


## Docker curl
{id: docker-curl}

{aside}
In the previous example we saw that we can use commands other than `echo`, but what if we would like to use `curl` for example?
It will fail because `curl` is not installed in the image.
{/aside}

* Let's try to use `curl`

```
$ docker run  --rm ubuntu:23.04 curl https://code-maven.com/
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

## Docker image as Curl command
{id: docker-curl-command}

{aside}
In the previous example we installed "curl" in Docker image so we could use it in the container, but we did not make any special arrangement for curl.
Using that image it is equally easy to run any other Linux command available in the image. What if we would like to make executing curl the default
behavior just as we had with `echo`?

We could include something like `CMD curl https://code-maven.com` in the Dockerfile, but then it would default to
download the given page.

We could use `CMD curl` and hope to pass the URL to the `docker run` command, but the parameters given on the command-line will override everything we have in CMD.

However there is another tool called `ENTRYPOINT`. It is very similar to `CMD`, but in certain situations it allows the *addition* of parameters
instead of the overwriting of parameters.
{/aside}

![](examples/curl-command/Dockerfile)

```
$ docker build -t mydocker .
```

* Run alone will execute `curl` without parameters:

```
$ docker run --rm  mydocker
curl: try 'curl --help' or 'curl --manual' for more information
```

* Supply the URL and that's it:

```
$ docker run --rm  mydocker https://code-maven.com/
```

## Docker: ENTRYPOINT vs CMD
{id: docker-entrypoint-vs-cmd}

![](examples/curl-runner/Dockerfile)

{aside}
By default if you run a container based on this image, Docker will execute a command which is a combination of the ENTRYPOING + CMD.

However, on the command-line where you call `docker run`, you can provide a replacement for the CMD part.
{/aside}

* Build the image:

```
$ docker build -t mydocker .
```

* Running container this way will execute `curl --silent https://httpbin.org/get`

```
$ docker run --rm  mydocker
```

* The user can replace the CMD part, so if we run this command, docker will execude `curl https://szabgab.com/`

```
$ docker run --rm  mydocker https://szabgab.com/
```

* [ENTRYPOINT](https://docs.docker.com/engine/reference/builder/#entrypoint)
* [CMD](https://docs.docker.com/engine/reference/builder/#cmd)

## Docker and environment variables with ENV
{id: docker-with-environment-variables}
{i: ENV}
{i: --env}

![](examples/env/Dockerfile)

{aside}
We can declare environment variables and give them values inside the Docker file using the ENV keyword.

When running docker we can override these and provide other environment varibles using the `--env` command-line parameter.
{/aside}


```
docker build -t mydocker .
```

```
$ docker run --rm mydocker
Foo
```

```
$ docker run --rm --env SECOND=Bar mydocker
Foo Bar
```

```
$ docker run --rm --env SECOND=Bar --env FIRST=Peti qqrq
Peti Bar
```

## Docker: Mounting external host directory as a volume (Linux, macOS hosts)
{id: docker-mounting-host-directory}

```
$ docker run -it --rm -v $(pwd):/opt/ mydocker

# cd /opt
# ls -l
```

The `-v HOST:CONTAINER` will mount the `HOST` directory of the home operating system to the `CONTAINER` directory in the Docker container.

## Docker: Mounting external host directory as a volume (Windows hosts)
{id: docker-mounting-host-directory-windows-host}

In CMD window:

```
> docker run -it --rm -v %cd%:/opt/ mydocker
```

In Power Shell:

```
> docker run -it --rm -v ${PWD}:/opt/ mydocker
```

In any case the path to the folder must only contain [a-zA-Z0-9_.-] character so no spaces, no Hebrew characters, etc.

## Docker build passing command-line argumens
{id: docker-build-passing-command-line-arguments}

We can defined command-line parameters in the Dockerfile and then allow the user who builds the
image to pass in values on the command line of `docker build`.

![](examples/arguments/Dockerfile)

```
docker build -t mydocker --build-arg TEXT=Bar .
```


## Exercies 2
{id: exercise-2}

Pick your favorite distribution (Ubuntu, Debian, CentOS, Fedora, etc.) and use it as the base of your application.

* Compile the most recent release of Python from source code (you will need to install some prerequisites).
* Add a Python based application using MongoDB or PostgreSQL or MySQL - whatever you like.
* Prepare it for distribution.

* Install NodeJS, express, create a small web app (hello world would suffice) and prepare it for distribution.

* Create a system of two Flask (or Express) applications that provide APIs and a third command-line application that accesses those APIs.


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


