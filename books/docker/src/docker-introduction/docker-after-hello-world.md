# After Hello World


no running containers, but there is one on the disk:

```
$ docker container ls -a -s
$ docker ps -as
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES               SIZE
f6239f10a6ad        hello-world         "/hello"            8 seconds ago       Exited (0) 7 seconds ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

* I keep fortgeting what does that `-s` do, so I run:

```
$ docker ps --help
```

There is also an image

```
$ docker images
$ docker image ls
$ docker image list
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
```


