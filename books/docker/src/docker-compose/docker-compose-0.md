# Docker compose


* up
* attach
* exec


The configuration of Docker compose is stored in a YAML file, usually called docker-compose.yml.
The following is a very simple example that defines a single Docker container, cleverly named "one"
which is based on the Ubuntu 20.04 image. Normally in order for a Docker container to keep running
you need to execute some command in them that will keep running. We can achieve the same by configuring
the stdin_open and the tty parameters. (They are the same as providing `-it` on the command line of
`docker`.)


{% embed include file="src/examples/interactive-shell/docker-compose.yml)


In order to launch the Docker containers we need to cd in the directory where we have the docker-compose.yml file and then
type in `docker-compose up`. This will download the image if necessary and launch the Docker container.


```
cd examples/interactive-shell
$ docker-compose up
```

In another terminal, but in the same directory you can run one-off commands on the running container:

```
$ docker exec interactive-shell_one_1 hostname
```

You can also attach to it:

```
$ docker attach interactive-shell_one_1
```

However, when you exit, it will shut down the container.


