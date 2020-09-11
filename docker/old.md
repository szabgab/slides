# Decomissioned Docker slides
{id: decomissioned-docker-slides}

## Installing Python in Docker
{id: installing-python-in-docker}

{aside}
This is a simple Ununtu-based Docker image into which we have installed python3.
We build it, we run it in interactive mode and then inside we can run python3.
{/aside}

![](examples/old-python-1/Dockerfile)

```
$ docker build -t mydocker1 .
```

```
$ docker run --rm -it mydocker1
# which python3
```

## Installing Python in Docker - one layer
{id: installing-python-in-docker-one-layer}

{aside}
The same as earlier, but now we merged the 3 RUN commands into one, so we have less levels in the history.
{/aside}

![](examples/old-python-2/Dockerfile)

```
$ docker build -t mydocker2 .
```

## Docker history
{id: docker-history-compare}

```
$ docker history mydocker1
```

![](examples/dock/history_mydocker1.out)

```
$ docker history mydocker2
```
![](examples/dock/history_mydocker2.out)


