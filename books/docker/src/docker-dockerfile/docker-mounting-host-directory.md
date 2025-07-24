# Docker: Mounting external host directory as a volume (Linux, macOS hosts)


```
$ docker run -it --rm -v $(pwd):/opt/ mydocker

# cd /opt
# ls -l
```

The `-v HOST:CONTAINER` will mount the `HOST` directory of the home operating system to the `CONTAINER` directory in the Docker container.


