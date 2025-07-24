# Docker and environment variables with ENV


* ENV
* --env

{% embed include file="src/examples/env/Dockerfile" %}


We can declare environment variables and give them values inside the Docker file using the ENV keyword.

When running docker we can override these and provide other environment varibles using the `--env` command-line parameter.



```
docker build -t mydocker .
```

```
$ docker run --rm mydocker
Foo
```

```
$ docker run --rm --env SECOND=Bar mydocker
Foo Bar
```

```
$ docker run --rm --env SECOND=Bar --env FIRST=Peti qqrq
Peti Bar
```


