# Docker container vs. image

* image
* container


In the world of Docker an **image** is a fixed version of an installed application while a **container** is a running copy of the image.

A Docker image is similar to an ISO image in the world of VirtualBox from which we can create an installation and then run it.
The Docker container in this description would be similar to the already virtual hard-disk a Virtual Server has.


You can download Docker images and you can build your own images based on already existing ones by installing more software on it or copying files to it.
It is frozen on the disk of your host computer.

When you run a Docker **image**, Docker creates a copy of it and we start to call it a **container**. A running instance of the image.
You can still install more applications on a container, but usually it is done only during development time.

Some people also try to use the class-instance analogy to the image-container pair. I am not sure how close is that, but that too is
just an approximation.


container = runtime of an image

* It is like instance = runtime class
* Or Virtual Machine = the running instance of an ISO file.


