# Crystal in Docker on Linux


* [Docker Crystal](https://hub.docker.com/r/crystallang/crystal)
* Install Docker
* Create a file called `crystal` with the following content:

{% embed include file="src/examples/crystal" %}

* Make it executable by running `chmod +x crystal`
* Run `./crystal examples/intro/hello_world.cr`

Alternative:

Start docker container:

```
docker run --rm -it -w/opt -v$(pwd):/opt --name crystal -d crystallang/crystal tail -f /opt/Dockerfile
```

Execute in the running container:

```
docker exec crystal crystal examples/intro/hello_world.cr
```

Later you can stop the container:

```
docker -t0 stop crystal
```


