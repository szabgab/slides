# Python Flask
{id: python-flask}


## Python Flask intro
{id: python-flask-intro}

* [Flask](http://flask.pocoo.org/)
* [Jinja](http://jinja.pocoo.org/)
* [Werkzeug](http://werkzeug.pocoo.org/)



## Flask: Hello World
{id: flask-hello-world}
![](examples/flask/hello_world.py)

```
$ python examples/flask/hello_world.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Flask hello world + test
{id: flask-hello-world-test}

![](examples/flask/hello_world/app.py)

![](examples/flask/hello_world/test_app.py)


## Flask generated page - time
{id: flask-generated-page-time}


![](examples/flask/time/time_app.py)


## Flask: Echo GET
{id: flask-echo-get}
![](examples/flask/echo_get.py)


## Flask: Echo POST
{id: flask-echo-post}

![](examples/flask/echo_post.py)
![](examples/flask/test_echo_post.py)


## Flask: templates
{id: flask-templates}
![](examples/flask/1/echo_post.py)
![](examples/flask/1/templates/index.html)

**Internal Server Error**



## Flask: Debug
{id: flask-debug}
![](examples/flask/1/echo_post_debug.py)


## Flask: templates
{id: flask-templates-work}
![](examples/flask/1/echo_post_work.py)


## Flask: templates with parameters
{id: flask-templates-parameters}
![](examples/flask/2/echo.py)
![](examples/flask/2/templates/echo.html)


## Flask: runner
{id: flask-runner}

* Remove the code that launches flask from within the application.


```
$ cd examples/flask/3
$ export FLASK_APP=hello.py
$ export FLASK_DEBUG=1
$ flask run
```


or



```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run
```

```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run --port 8080 --host 0.0.0.0
```
![](examples/flask/3/echo.py)
![](examples/flask/3/templates/echo.html)


## Exercise: Flask calculator
{id: exercise-flask-calculator}

Write a web application that has two entry boxes and a button and
that will add the two numbers inserted into the entry boxes.




## Static files
{id: flask-static-files}
![](examples/flask/4/app.py)
![](examples/flask/4/templates/main.html)
![](examples/flask/4/templates/other.html)


## Flask: Counter
{id: flask-counter}
![](examples/flask/10/counter.py)


Access the page from several browsers. There is one single counter that lives as long as the process lives.




## Flask Logging
{id: flask-logging}
![](examples/flask/5/app.py)


## Color selector without session
{id: flask-no-session}
![](examples/flask/11/color.py)
![](examples/flask/11/templates/main.html)


## Session management
{id: flask-session}
![](examples/flask/11/app.py)



## Flask custom 404 page
{id: flask-404-page}

FLASK_APP=app.py FLASK_DEBUG=1  flask run

![](examples/flask/12/app.py)

```
curl -I http://localhost:5000/not

HTTP/1.0 404 NOT FOUND
```


## Flask Error page
{id: flask-error-page}
![](examples/flask/13/app.py)

```
$ FLASK_APP=echo.py FLASK_DEBUG=0  flask run
```

```
curl -I http://localhost:5000/not

HTTP/1.0 500 INTERNAL SERVER ERROR
```



## Flask Path params
{id: flask-path-params}
![](examples/flask/15/app.py)


## Flask Path params (int)
{id: flask-path-params-int}
![](examples/flask/16/app.py)


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

