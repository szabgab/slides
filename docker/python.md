# Python with Docker
{id: python-with-docker}

## Python CLI in Docker - curl.py
{id: python-cli-in-docker-code}

![](examples/python-3/curl.py)

## Python CLI in Docker - curl.py
{id: python-cli-in-docker-dockerfile}


![](examples/python-3/Dockerfile)

```
$ docker build -t mydocker .
```

```
docker run --rm mydocker https://httpbin.org/get
```

{aside}
This is a simple implementation of a curl-like script in Python. Wrapped in a Docker container. Firs build the container and then you can run the script.
{/aside}

## Docker: Mounting host directory
{id: docker-mounting-host-directory}

```
$ docker run -it --rm -v /home/gabor/work/slides/docker/examples/python-3:/opt/  mydocker

$ docker run -it --rm -v c:\Users\Gabor Szabo\work\slides\docker\examples python-3:/opt/  mydocker

# cd /opt
# ls -l
```

The `-v HOST:CONTAINER` will mount the `HOST` directory of the home operating system to the `CONTAINER` directory in the Docker container.

```
# ./curl.py -I https://code-maven.com/slides
```

* You can edit the file on your host system (with your IDE) and run it on the command line of the Docker container.


* A better way to mount the current working directory, at least on Linux and OSX

```
docker run -it --rm -v $(pwd):/opt/  mydocker
```


## Distribute command-line script
{id: distribute-command-line-script}


![](examples/python-4/Dockerfile)

```
$ docker build -t mydocker .

$ docker run --rm   mydocker /opt/curl.py https://code-maven.com/slides
```

## Distribute command-line script and include command
{id: distribute-command-line-script-and-include-command}

![](examples/python-5/Dockerfile)


```
$ docker build -t mydocker .


$ docker run --rm   mydocker https://code-maven.com/slides
```


## Flask application
{id: flask-application}

![](examples/flask-development/app.py)

![](examples/flask-development/templates/echo.html)

![](examples/flask-development/requirements.txt)


## Flask development
{id: flask-development}

![](examples/flask-development/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --name dev --rm -p:5001:5000 -v $(pwd):/opt/  mydocker
```

Access via [http://localhost:5001/](http://localhost:5001/)

The -it is needed so we can see the log on the command line and we can easily stop the development container.



## Docker: Flask + uwsgi
{id: flask-uwsgi}

![](examples/flask-uwsgi/Dockerfile)

![](examples/flask-uwsgi/uwsgi.ini)

## Docker: Flask + uwsgi + nginx
{id: flask-uwsgi-nginx}

Using [https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)

```
docker build -t myapp .
docker run -it --rm -p5001:80 myapp
```

## Flask with Redis
{id: flask-with-redis}

![](examples/flask-redis/app.py)
![](examples/flask-redis/templates/red.html)
![](examples/flask-redis/requirements.txt)


## Docker compose Flask and Redis
{id: docker-compose-redis-flask}

```
pip install docker-compose
```

![](examples/flask-redis/docker-compose.yml)
![](examples/flask-redis/Dockerfile)

```
docker-compose up
```

* http://localhost:5001/

## Python Flask and MongoDB
{id: python-flask-mongodb}

![](examples/flask-mongodb/app.py)
![](examples/flask-mongodb/templates/main.html)
![](examples/flask-mongodb/requirements.txt)
![](examples/flask-mongodb/Dockerfile)
![](examples/flask-mongodb/docker-compose.yml)

```
docker-compose up
```

* http://localhost:5001/


## Python, Flask and Pulsar
{id: python-flask-and-pulsar}

```
docker run -it -p 6650:6650 -p 8080:8080  apachepulsar/pulsar:2.4.1 bin/pulsar standalone
docker build -t mydocker .
docker run --rm -it mydocker bash
```

![](examples/python-pulsar/docker-compose.yml)

![](examples/python-pulsar/Dockerfile)

![](examples/python-pulsar/pulsar_demo.py)

## Python and Pulsar
{id: python-and-pulsar}

![](examples/python-pulsar-cli/consumer.py)
![](examples/python-pulsar-cli/docker-compose.yml)
![](examples/python-pulsar-cli/Dockerfile)
![](examples/python-pulsar-cli/input.txt)
![](examples/python-pulsar-cli/mytools.py)
![](examples/python-pulsar-cli/producer.py)
![](examples/python-pulsar-cli/requirements.txt)

Run:

```
docker-compose up
```

and then check the pulsar.log file

