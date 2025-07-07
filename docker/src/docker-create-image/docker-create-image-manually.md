# Docker create image manually

We went over this step-by-step earlier, but let's have all the step in one place:


* Run container interactively (based on Ubuntu 23.04, call it ubu)

```
docker run -it --name ubu ubuntu:23.04
```

* Install packages, copy or create files, etc..., exit.

```
# apt-get update
# apt-get install htop
# echo "Hello World" > welcome.txt
# exit
```

* Create the image called myubu from the container called ubu

```
docker container commit ubu myubu:1.00
```

* Run a container based on the new image called myubu:

```
docker container run --rm -it myubu:1.00
```


