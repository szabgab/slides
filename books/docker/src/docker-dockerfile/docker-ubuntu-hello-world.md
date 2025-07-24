# Docker: Ubuntu Hello World

* CMD


Having an image identical to some already existing image does not give us a lot of value, so let's create make another small step.
Let's add another instruction to the Dockerfile called `CMD`. The content of the `CMD` line is not executed when we build the image.
Whatever comes after this `CMD` will be executed when we start the Docker container based on this image. Unless we override it.

In our case we just use the shell command `echo` to print "hello world" to the screen.


{% embed include file="src/examples/hello-world/Dockerfile" %}

```
$ docker build -t mydocker .
```


Once the image is ready we can run it and it will print out "hello world" as expected. You could distribute this image to show that you made it!
Well, we have not seen yet how to distribute the image, but aside of that everything is fine.


```
$ docker run --rm mydocker
hello world
```


The user of this new image can provide her own command on the command line, either another echo command or something
totally different such as the `pwd` below.


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


