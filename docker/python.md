# Python with Docker
{id: python-with-docker}

## Installing Python in Docker
{id: installing-python-in-docker}

{aside}
This is a simple Ununtu-based Docker image into which we have installed python3.
We build it, we run it in interactive mode and then inside we can run python3.
{/aside}

![](examples/python-1/Dockerfile)

```
$ docker build -t mydocker1 .
```

```
$ docker run --rm -it mydocker1
# which python3
```

## Installing Python in Docker - one layer
{id: installing-python-in-docker-one-layer}

{aside}
The same as earlier, but now we merged the 3 RUN commands into one, so we have less levels in the history.
{/aside}

![](examples/python-2/Dockerfile)

```
$ docker build -t mydocker2 .
```

## Docker history
{id: docker-history-compare}

```
$ docker history mydocker1
```

![](examples/dock/history_mydocker1.out)

```
$ docker history mydocker2
```
![](examples/dock/history_mydocker2.out)

## Python CLI in Docker
{id: python-cli-in-docker}

![](examples/python-3/curl.py)

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

