# Docker: Empty Ubuntu


* FROM


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


{% embed include file="src/examples/from/Dockerfile" %}

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
```


