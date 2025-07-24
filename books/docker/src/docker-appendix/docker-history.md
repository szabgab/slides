# Docker history



Each Docker image is built by layers upon layers.

The `docker history` command can show you these layers.


```
docker history IMAGE
```


Here you can see that the Ubuntu image we have downloaded from the Docker Hub has 5 layers.


```
$ docker history ubuntu:20.04
```

{% embed include file="src/examples/dock/history_ubuntu.out" %}


