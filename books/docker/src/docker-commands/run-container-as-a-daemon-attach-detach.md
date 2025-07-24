# Run container as a daemon - attach detach


* attach
* -d
* exec

* Run as a Daemon in the background name it 'test'

```
docker run -d --rm -it --name test busybox
```

* Check if it is running using `docker ps`

Run things on it

```
docker exec CONTAINER command   (eg ls, cat ...)
```


* Attach to it:

```
docker container attach test
```

* Detach from the container and keep it running by pressing

```
Ctrl-p Ctrl-q
```


