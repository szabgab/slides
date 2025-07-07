# Docker: Python Development mode with mounted directory

{% embed include file="src/examples/python-curl-dev/Dockerfile" %}

```
$ docker build -t mydocker .

$ docker run --rm -v $(pwd):/opt/ mydocker python /opt/curl.py  https://httpbin.org/get
```

* `--rm` to remove the container when we stopped it.
* `-v $(pwd):/opt/` to map the current directory on the host system to the /opt directory inside the container
* `mydocker` is the name of the image
* After that we can any python program.

* You can edit the file on your host system (with your IDE) and run it on the command line of the Docker container.
* This works on Linux and Mac OSX. On Windows you might need to spell out the current working directory yourself.


