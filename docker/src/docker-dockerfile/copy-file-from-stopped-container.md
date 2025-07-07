# Copy file from stopped container

* copy
* cp


At this point we could get back to the container and verify that the file is still there, and I encourage you do that,
but we would like to do something else as well. We would like to be able to see the file even though the container
does not run any more. We can do this by running the `docker container cp` command.

The command gets two parameters, the first one contains the name of the container and the path to the file
inside the container we would like to copy. The second parameter is the name or location of the file outside
the container. dot `.` just means, copy the file here with the same name as we had inside.

The `cp` command looks similar to the `cp` command of Linux.


```
docker container cp CONTAINER_NAME:FILE .
docker container cp ubu:welcome.txt .
```

* On your host OS you can copy files from the container to the external filesystem.



