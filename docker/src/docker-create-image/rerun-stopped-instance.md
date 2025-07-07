# Rerun (restart) stopped instance


* container
* start


It is great that we have a container on the disk which is not runnin any more, but what can we do with it?

Probably the most important thing is that we can re-launch it. Type in `docker container start -i ubu` and
you'll be back inside the same container. How do you know it is the same?  You can run `htop` and see it is installed.
If you were running a new container you'd have no `htop` installed as that's not part of the Ubuntu image as
it was downloaded from the Docker hub.



```
docker container start -i ubu
docker container start -i CONTAINER
```


