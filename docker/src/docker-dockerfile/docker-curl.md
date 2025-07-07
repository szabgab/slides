# Docker curl

In the previous example we saw that we can use commands other than `echo`, but what if we would like to use `curl` for example?
It will fail because `curl` is not installed in the image.


* Let's try to use `curl`

```
$ docker run  --rm ubuntu:23.04 curl https://code-maven.com/
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "exec: \"curl\": executable file not found in $PATH": unknown.
```


To install it we need to add `RUN` commands. (Yeah, I know the name might be a bit confusing, but think about it from the point of view of the build process.
We would like to run something during the build process.)

In order to install the `curl` package in Ubuntu we need to execute the `apt-get install -y curl` command.
(The `-y` flag is there so `apt-get` will not ask for confirmation.)
However before we can execute that command we need to download the list of all the available packages. We do that by running (here is that word!)
the `apt-get update` command.

We don't have a `CMD` as we don't have a default operation.


{% embed include file="src/examples/curl/Dockerfile" %}


We can build the image the same way we built the previous one.


```
$ docker build -t mydocker .
```


Then we can run it. This time it will execute the `curl` command.


```
$ docker run  --rm mydocker curl https://code-maven.com/
```



