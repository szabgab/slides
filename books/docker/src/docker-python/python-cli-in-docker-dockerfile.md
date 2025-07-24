# Python CLI in Docker - Dockerfile


* [python](https://hub.docker.com/_/python)

{% embed include file="src/examples/python-curl/Dockerfile" %}

```
$ docker build -t mydocker .

$ docker run --rm mydocker https://httpbin.org/get
```

* [https://httpbin.org/](https://httpbin.org/)


This is a simple implementation of a curl-like script in Python. Wrapped in a Docker container. First build the container and then you can run the script.


