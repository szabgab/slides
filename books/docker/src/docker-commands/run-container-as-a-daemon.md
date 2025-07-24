# Run container as a daemon

* inspect
* logs


In this example we create a Docker image based on busybox and tiny bit of shell command.
Specifically we'll run an infinite while-loop and every second we'll print the current date and time.

The first thing we need to do is to build the


{% embed include file="src/examples/daemon1/Dockerfile" %}

```
docker build -t mydocker .
docker run -d --rm --name test mydocker
docker inspect test
docker container logs test
docker container attach test
Ctrl-p Ctrl-q
```


