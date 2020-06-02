# Python with Docker
{id: python-with-docker}

## Installing Python in Docker
{id: installing-python-in-docker}

![](examples/python-1/Dockerfile)

```
$ docker build -t mydocker .

$ docker run --rm -it mydocker
# which python3
```

## Installing Python in Docker - one layer
{id: installing-python-in-docker-one-layer}

![](examples/python-2/Dockerfile)

```
$ docker build -t mydocker2 .
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


