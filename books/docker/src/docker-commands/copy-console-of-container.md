# Copy console output of container (logs)

* logs

```
docker logs CONTAINER_ID
```

* [logs](https://docs.docker.com/engine/reference/commandline/logs/)

 - [Ignore files and directories](./docker-commands/ignore-files-and-directories.md)
* .dockerignore}

`docker build .`   will send over all the content of the corrent directory to the docker
daemon. You usually don't want that. So add a file called `.dockerignore` to the root
of your project

```
.git/
temp/
```


