# Dockerfile


```
Dockerfile
```

```
FROM debian
RUN apt-get update
RUN apt-get install -y htop
RUN apt-get install -y curl
```

```
docker build -t exp1 .
docker images
docker history exp1
docker run --rm -it exp1
```


