# Create image from container

* commit


Now that we have a conatainer with all the necessary packages installed (htop)
and all the necessary files created (welcome.txt) let's convert this container
into an image. Let's freeze this container so it will become reusable.
Either by me or by others as well.

We can do this by running the `docker container commit` command. It needss to get
the name of the contain as the base-container and the name and tag of the
new image. Here I used the name "myubu"

Once we have the new image we can list it using the `docker images` command and we can
run it with the regular `run` command.


```
docker container commit CONTAINER IMAGE
docker container commit ubu myubu:1.00
```

```
docker images
docker container run --rm -it myubu:1.00
```


