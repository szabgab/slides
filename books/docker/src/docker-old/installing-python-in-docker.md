# Installing Python in Docker


This is a simple Ununtu-based Docker image into which we have installed python3.
We build it, we run it in interactive mode and then inside we can run python3.


{% embed include file="src/examples/old-python-1/Dockerfile" %}

```
$ docker build -t mydocker1 .
```

```
$ docker run --rm -it mydocker1
# which python3
```


