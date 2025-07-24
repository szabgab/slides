# Download image


* pull


Earlier when we used the `run` command to run a Docker images, the first thing it did was downloading the image.
Subsequent `run` commands only executed the image.

You could actully download images without running them using the `pull` command. You only need to provide the name and the tag
of the image.


```
docker pull ubuntu:23.04
```


