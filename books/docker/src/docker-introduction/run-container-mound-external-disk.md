# Run container mount external disk



```
docker run --rm "-v%CD%:/opt" -w /opt -it busybox
```

* -w to set the default workdir inside the container
* -v to mount an external folder to an internal folder
* %CD% is the current folder in Windows (outside)
* /opt is the folder inside
* We need double-quotes around it as the currecnt working directory on windows can contain spaces and other special characters.
* --rm to remove the container at the end of the run
* -it interactive mode


