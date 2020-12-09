# Python with Docker
{id: python}

## Python CLI in Docker - curl.py
{id: python-cli-in-docker-code}

{aside}
This is a command line script, a very basic implementation of curl in Python. In order to run this we need Python and the `requests` package to be installed.
{/aside}

![](examples/python-curl/curl.py)

## Python CLI in Docker - Dockerfile
{id: python-cli-in-docker-dockerfile}

* [python](https://hub.docker.com/_/python)

![](examples/python-curl/Dockerfile)

```
$ docker build -t mydocker .

$ docker run --rm mydocker https://httpbin.org/get
```

* [https://httpbin.org/](https://httpbin.org/)

{aside}
This is a simple implementation of a curl-like script in Python. Wrapped in a Docker container. First build the container and then you can run the script.
{/aside}


## Docker: Python Development mode with mounted directory
{id: docker-development-mode-with-mounted-directory}


![](examples/python-curl-dev/Dockerfile)

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


## Flask application
{id: flask-application}

{aside}
In this simple Flask web application we have 3 files. app.py, a template, and the requirements.txt
{/aside}

![](examples/flask-development/app.py)

![](examples/flask-development/templates/echo.html)

![](examples/flask-development/requirements.txt)


## Flask development
{id: flask-development}

![](examples/flask-development/Dockerfile)

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


## Docker: Flask + uwsgi
{id: flask-uwsgi}

![](examples/flask-uwsgi/Dockerfile)

![](examples/flask-uwsgi/uwsgi.ini)

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
![](examples/flask-mongodb/requirements.txt)

![](examples/flask-mongodb/templates/main.html)
![](examples/flask-mongodb/templates/list.html)
![](examples/flask-mongodb/templates/person.html)
![](examples/flask-mongodb/templates/404.html)
![](examples/flask-mongodb/templates/incl/header.html)
![](examples/flask-mongodb/templates/incl/footer.html)

## Docker Compose Python Flask and MongoDB
{id: docker-compose-python-flask-mongodb}

```
pip install docker-compose
```

* [mongo](https://hub.docker.com/_/mongo)

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

## Docker: Flask + uwsgi + nginx
{id: flask-uwsgi-nginx}

Using [https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/](https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask/)

```
docker build -t myapp .
docker run -it --rm -p5001:80 myapp
```
