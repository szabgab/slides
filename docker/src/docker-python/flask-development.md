# Flask development


{% embed include file="src/examples/flask-development/Dockerfile" %}

```
$ docker build -t mydocker .
$ docker run -it --name dev --rm -p5001:5000 -v $(pwd):/opt/  mydocker
```

* `-it` to be in interactive mode so we can see the log on the command line and we can easily stop the development container.
* `--name dev` we set the name of the container to be `dev` in case we would like to access it.
* `--rm` remove the container after it is finished.
* `-p5001:5000` map port 5001 of the host computer to port 5000 of the container.
* `-v $(pwd):/opt/` map the current working directory of the host to /opt in the container.

* Access via [http://localhost:5001/](http://localhost:5001/)


