# Docker: Ubuntu htop

* RUN


Previously we created a Docker image manually after we have installed `htop` and created a file manually in a Docker container.
Let's do the same now using Dockerfile.


{% embed include file="src/examples/ubuntu-htop/Dockerfile" %}

```
docker build -t mydocker .
docker run --rm -it mydocker
```


