# Docker create image manually - placeholders


* Run conatiner

```
docker run -it --name NAME BASE_CONTAINER:BASE_TAG
```

* install stuff in the container, copy stuff to the container, exit

* Create image from container

```
docker container commit CONTAINER NEW_IMAGE_NAME:TAG
```

* Better yet, create the container under your Docker Hub username:

```
docker container commit CONTAINER USERNAME/NEW_IMAGE_NAME:TAG
```

* To verify, run a container based on the new image (with or without username):

```
docker container run --rm -it NEW_IMAGE_NAME:TAG
docker container run --rm -it USERNAME/NEW_IMAGE_NAME:TAG
```


