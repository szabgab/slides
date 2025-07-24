# Use Ubuntu to run a single command



As earlier we saw how to use the **busybox** image, but most people are not familiar with busybox, so let's see a few examples
using the Ubuntu image. We are still not building our own image at this point, just playing with a ready-made image.

The `run` command allows us to launch a Docker container based on an image. The `--rm` flag tells Docker to remove the container from
ou harddisk once it stopped running. It is a good idea to do so if you don't need the conatainer any more. Otherwise the dead containers
would just accumulate and take up disk space.

After the name of the image we can also provide the command line that needs to be execute. In this case `echo hello` is just a simple shell command.

Running this will print `hello` and then the conatiner will exit and it will be removed from the disk as if it never existed.


```
docker run --rm ubuntu:23.04 echo hello
```


