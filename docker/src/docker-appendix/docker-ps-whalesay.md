# Docker ps after whalesay


```
$ docker ps -as

CONTAINER ID        IMAGE               COMMAND                CREATED             STATUS                      PORTS               NAMES
59c99df0177a        docker/whalesay     "cowsay hello world"   36 minutes ago      Exited (0) 23 minutes ago                       loving_wescoff      0 B (virtual 247 MB)
f6239f10a6ad        hello-world         "/hello"               About an hour ago   Exited (0) 58 minutes ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              48b5124b2768        6 weeks ago         1.84 kB
docker/whalesay     latest              6b362a9f73eb        21 months ago       247 MB
```


