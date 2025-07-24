# Volumes


* [volumes](https://docs.docker.com/storage/volumes/)

docker run --mount source=myvol,target=/data --rm -it busybox

```
docker volume ls --format "{{.Driver}}  {{.Name}} {{.Mountpoint}}"

docker volume create myvol
    Creates /var/lib/docker/volumes/myvol

docker volume ls
docker volume inspect myvol  # Returns a JSON with information about the volume
docker volume rm myvol


docker-compose up
docker-compose rm

```


