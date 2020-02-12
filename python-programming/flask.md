# Python Flask
{id: python-flask}


## Python Flask intro
{id: python-flask-intro}
{i: Flask}
{i: Jinja}
{i: Werkzeug}

* [Flask](http://flask.pocoo.org/)
* [Jinja](http://jinja.pocoo.org/)
* [Werkzeug](http://werkzeug.pocoo.org/)

## Python Flask installation
{id: python-flask-installation}

```
virtualenv venv -p python3
source venv/bin/activate

pip install flask
```


## Flask: Hello World
{id: flask-hello-world}

![](examples/flask/hw/hello_world.py)

```
$ python hello_world.py
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Flask hello world + test
{id: flask-hello-world-test}

![](examples/flask/hello_world/app.py)

```
FLASK_APP=app FLASK_DEBUG=1 flask run

Visit: http://127.0.0.1:5000/
curl http://localhost:5000/
```

Windows on the command line or in the terminal of Pycharm.

```
set FLASK_APP=app
set FLASK_DEBUG=1
flask run
```

![](examples/flask/hello_world/test_app.py)

```
pytest
```

## Flask generated page - time
{id: flask-generated-page-time}


![](examples/flask/time/app.py)
![](examples/flask/time/test_app.py)


## Flask: Echo GET
{id: flask-echo-get}


![](examples/flask/echo_get/app.py)
![](examples/flask/echo_get/test_app.py)

```
curl http://localhost:5000/
curl http://localhost:5000/echo?text=Sanch+Panza
```

![](examples/flask/echo_get/client.py)


## Flask: Echo POST
{id: flask-echo-post}

![](examples/flask/echo_post/app.py)
![](examples/flask/echo_post/test_app.py)

```
curl --data "text=Sancho Panza" http://localhost:5000/echo
```

![](examples/flask/echo_post/client.py)


## Flask: templates
{id: flask-templates}

![](examples/flask/tmpl/echo_post.py)
![](examples/flask/tmpl/templates/index.html)

```
FLASK_APP=echo_post FLASK_DEBUG=0 flask run
```
**Internal Server Error**

```
FLASK_APP=echo_post FLASK_DEBUG=1 flask run
```

## Flask: templates
{id: flask-templates-work}

![](examples/flask/tmpl/echo_post_work.py)


## Flask: templates with parameters
{id: flask-templates-parameters}


![](examples/flask/params/echo.py)
![](examples/flask/params/templates/echo.html)
![](examples/flask/params/test_echo.py)


## Flask: runner
{id: flask-runner}

```
$ cd examples/flask/params
```

```
$ export FLASK_APP=echo
$ export FLASK_DEBUG=1
$ flask run
```

or


```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run
```

on windows

```
> set FLASK_APP=echo
> set FLASK_DEBUG=1
> flask run
```

Other parameters

```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run --port 8080 --host 0.0.0.0
```

## Exercise: Flask calculator
{id: exercise-flask-calculator}

Write a web application that has two entry boxes and a button and
that will add the two numbers inserted into the entry boxes.


## Static files
{id: flask-static-files}

![](examples/flask/st/app.py)
![](examples/flask/st/templates/main.html)
![](examples/flask/st/templates/other.html)

```
.
├── app.py
├── static
│   └── img
│       └── python.png
└── templates
    ├── main.html
    └── other.html
```



## Flask Logging
{id: flask-logging}

![](examples/flask/log/app.py)

## Flask: Counter
{id: flask-counter}

![](examples/flask/counter/app.py)

Access the page from several browsers. There is one single counter that lives as long as the process lives.


## Color selector without session
{id: flask-no-session}

![](examples/flask/color/color.py)
![](examples/flask/color/templates/main.html)


## Session management
{id: flask-session}

![](examples/flask/color/app.py)


## Flask custom 404 page
{id: flask-404-page}

![](examples/flask/404/app.py)
![](examples/flask/404/app404.py)

```
curl -I http://localhost:5000/not

HTTP/1.0 404 NOT FOUND
```


## Flask Error page
{id: flask-error-page}

![](examples/flask/500/app.py)

Will not trigger in debug mode!

```
$ FLASK_APP=echo.py FLASK_DEBUG=0  flask run
```

```
curl -I http://localhost:5000/not

HTTP/1.0 500 INTERNAL SERVER ERROR
```

![](examples/flask/500/app500.py)


## Flask Path params
{id: flask-path-params}

![](examples/flask/path/app.py)

## Flask Path params (int)
{id: flask-path-params-int}

![](examples/flask/path-int/app.py)

## Flask Path params add (int)
{id: flask-path-params-add-int}

![](examples/flask/path-int-add/app.py)


## Flask login
{id: flask-login}

![](examples/flask/17/app.py)
![](examples/flask/17/templates/account.html)
![](examples/flask/17/templates/header.html)
![](examples/flask/17/templates/home.html)
![](examples/flask/17/templates/login.html)
![](examples/flask/17/templates/logout.html)
![](examples/flask/17/templates/main.html)


## Flask JSON API
{id: flask-json-api}
![](examples/flask/20/app.py)

```
$ curl -I http://localhost:5000/api/info
HTTP/1.0 200 OK
Content-Type: application/json
```


## Flask and AJAX
{id: flask-and-ajax-plain-javascript}
![](examples/flask/21/app.py)
![](examples/flask/21/static/math.js)
![](examples/flask/21/templates/main.html)


## Flask and AJAX
{id: flask-and-ajax-jquery}
![](examples/flask/22/app.py)
![](examples/flask/22/static/math.js)
![](examples/flask/22/templates/main.html)


## passlib
{id: passlib}
![](examples/flask/use_passlib.py)

```
$ python use_passlib.py "my secret"
$pbkdf2-sha256$29000$svZ.7z2HEEJIiVHqPeecMw$QAWd8P7MaPDXlEwtsv9AqhFEP2hp8MvZ9QxasIw4Pgw
$pbkdf2-sha256$29000$XQuh9N57r9W69x6jtDaG0A$VtD35zfeZhXsE/jxGl6wB7Mjwj/5iDGZv6QC7XBJjrI
True
True
```


## Flask Testing
{id: flask-testing}
![](examples/flask/40/app.py)
![](examples/flask/40/test_app.py)


## Flask Deploy app
{id: flask-deploy}
![](examples/flask/50/app.py)

[uwsgi](https://uwsgi-docs.readthedocs.io/)

![](examples/flask/50/uwsgi.ini)

[nginx](https://nginx.org/)

![](examples/flask/50/nginx.conf)


## Exercise: Flask persistent
{id: exercise-flask-persistent-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing.




## Exercise: Flask persistent
{id: exercise-flask-persistent-multi-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing. For each user have its own counter as identified by the username they type in.


## Flask Simple Authentication + test
{id: flask-simple-authentication-test}
{i: HTTPBasicAuth}
{i: flask_httpauth}
{i: werkzeug.security}
{i: generate_password_hash}
{i: check_password_hash}

![](examples/flask/simple_auth/app.py)

![](examples/flask/simple_auth/test_app.py)

## Flask REST API
{id: flask-rest-api}

* [flask-restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

## Flask REST API - Echo
{id: flask-rest-api-echo}

![](examples/flask/api_echo/api.py)
![](examples/flask/api_echo/test_api.py)

## Flask REST API - parameters in path
{id: flask-rest-api-parameters-in-path}

![](examples/flask/api_path/api.py)
![](examples/flask/api_path/test_api.py)


## Flask REST API - parameter parsing
{id: flask-rest-api-parameter-parsing}

![](examples/flask/api_paremeters/api.py)
![](examples/flask/api_paremeters/test_api.py)

## Flask REST API - parameter parsing - required
{id: flask-rest-api-parameter-parsing-required}

![](examples/flask/api_paremeters_required/api.py)
![](examples/flask/api_paremeters_required/test_api.py)


## Flask Exercises
{id: flask-exercises}

* [Shopping list](https://code-maven.com/shopping-list)
* [TODO](https://code-maven.com/todo)

