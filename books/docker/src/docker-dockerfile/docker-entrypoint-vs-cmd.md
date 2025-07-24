# Docker: ENTRYPOINT vs CMD


{% embed include file="src/examples/curl-runner/Dockerfile" %}


By default if you run a container based on this image, Docker will execute a command which is a combination of the ENTRYPOING + CMD.

However, on the command-line where you call `docker run`, you can provide a replacement for the CMD part.


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


