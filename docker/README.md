* Show some interactive usage of Docker
* Commands on the command-line
* Show some cases with Dockerfile


- see the log files (/var/log/...) while the container is running, after the container has ended.
- In a production system, how do we collect (error) reports from containers?
- upload to server for production



Original hello-world is 1.84 kB
The one based onUbuntu is 121Mb

Distribute a web application (just flask)
Distribute a web application flask + nginx
Distribute a web application flask + nginx + MongoDB
Create an image with all the dependencies of a build and then reuse that image in every later stage. Rebuild the base image whenever the requirements file was changed.
docker pull
Create an image in the repository (from github)


## Run container as a daemon
{id: run-container-as-a-daemon}

```
docker run -d --rm busybox sleep 30

docker run --name my_name busybox sleep 100

docker inspect CONTAINER_ID
docker logs CONTAINER_ID
```


That's really nice, but once we close the container we lose our changes.
When we run again we need to start from scratch.
