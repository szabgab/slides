# Python Flask
{id: flask}


## Python Flask intro
{id: python-flask-intro}
{i: Flask}
{i: Jinja}
{i: Werkzeug}

{aside}
Flask is a light-weight web micro-framework in Python. By default it uses a templating system called Jinja and a WSGI web application library called Werkzeug.

In Flask you map URL paths to functions so when someone reaches the endpoint defined by the path the specific function is executed.
The function is expected to return the HTML to be displayed.

It is very easy to get started with Flask both if you'd like to build a web-site with HTML pages or if you are interested in providing an API that returns JSON.
{/aside}

* [Flask](https://flask.palletsprojects.com/)
* [Jinja](https://jinja.palletsprojects.com/)
* [Werkzeug](https://werkzeug.palletsprojects.com/)

## Python Flask installation
{id: python-flask-installation}

```
virtualenv venv -p python3
source venv/bin/activate

pip install flask
```

## Flask: Hello World
{id: flask-hello-world}

{aside}
The de-facto standard first thing to do in programming in every language or framework is to print "Hello World" on the screen.
This is what we are going to do with Flask now. This is probably the most simple Flask application.

For this we need to create regular Python file, for example **app.py**. I'd recommend you first create a new empty directory and
put the file inside that directory.

The first thing is to load the **Flask** class from the **flask** module.

Then we create an object representing the whole application. You could use any variable name for this, but the "standard" is to use
the name **app**.

Then comes the interesting part. We declare a function that will return the HTML page.
In our example the name of the function is **main**, but the name actually is not important. You could as well call it **some_other_name**.
The important part is the decorator above it. That decorator means that if someone reaches the path `/` on the web site, this function will
be executed and whatever it returns will be sent back to the browser. This mapping of a path to a function is called URL **routing** and we'll
discuss it in detail later on.

For now, let's see how we can use this.
{/aside}


![](examples/flask/hello_world/app.py)

## Flask: Run Hello World
{id: flask-run-hello-world}
{i: FLASK_DEBUG}
{i: FLASK_APP}
{i: run}

{aside}
In order to run this we need to set the environment variable **FLASK_APP** to the name of the file without the extension.
We can also set the **FLASK_DEBUG** environment variable to 1 tuning on the debug-mode, but this is not required for this example.

Then we execute `flask run`.

It is a bit different how you do this on Linux or Mac vs. on MS Windows.

In either case once flask is running you can use your browser to visit your new web application on http://127.0.0.1:5000/
You can also use `curl` on the command line to see the content of the web page.

Once you have enough, you can hit Ctr-C to stop the program.
{/aside}

Linux/Mac:

```
FLASK_APP=app FLASK_DEBUG=1 flask run

Visit: http://127.0.0.1:5000/
curl http://localhost:5000/
```

Windows on the command line or in the terminal of Pycharm:

```
set FLASK_APP=app
set FLASK_DEBUG=1
flask run
```

* To stop it use `Ctrl-C`

## Flask: testing hello world
{id: flask-hello-world-test}

{aside}
Before we go ahead learning how to create more complex web applications we need to learn another very important feature of Flask.

Flask makes it very easy to test your web application without even running a web server.

For this we created a file called `test_app.py` in the same folder as we have the `app.py` with the following content.
The name of the files must start with the word `test_`, but otherwise you can pick any filename.

Inside we import the application and we have a test function, again its name must start with `test_`. From the `app`
we can get the `test_client` which is a representation of our running web application.

Then we can send in various requests. In this case we sent in an HTTP GET request to the root of the site.

We get back a response object that we can then interrogate with various assertions.

To run this we'll need to install `pytest` and then we can just type in `pytest`. It will find and run the tests.
{/aside}

![](examples/flask/hello_world/test_app.py)

```
pytest
```

## Flask generated page - time
{id: flask-generated-page-time}

{aside}
Showing a static text in the previous example was already a success, but we would like to be able to have more dynamic web site.
In this example we'll see how to display the current time.

We have the same skeleton as in the previous example, but this time the `main` function serving the root path returns some HTML
that will be displayed as a link to the `/time` path.

We also have a second route mapping the `/time` path to the `show_time` function.

We run the application the same way as before on the command line.

Now if we access the `http://127.0.0.1:5000/` URL we'll see the text `time` that we can click on. When we click on it we arrive to the
`http://127.0.0.1:5000/time` page that shows the current time. Actually it will show the number of seconds from the epoch,
which is January 1, 1970, 00:00:00 (UTC).

Something like this: 1594528012.7892551
{/aside}

![](examples/flask/time/app.py)

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```

## Flask generated page - time tested
{id: flask-generated-page-time-tested}


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

## Flask URL routing
{id: flask-url-routing}

{aside}
The mapping of the path part of a URL, so the one that comes after the domain name and
after the port number (if it is included) is the path. Mapping that to a function call
is called routing.

In the following pages we are going to see several examples on how to map routes to functions.

It is also called "url route registration".
{/aside}

## Flask Path params
{id: flask-path-params}

![](examples/flask/path/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

## Flask Path params (int)
{id: flask-path-params-int}
{i: int}

![](examples/flask/path-int/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```


## Flask Path params add (int)
{id: flask-path-params-add-int}

![](examples/flask/path-int-add/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

## Flask Path params add (path)
{id: flask-path-params-any-path}
{i: path}

* Accept any path, including slashes:

![](examples/flask/path-any/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```


## Jinja loop, conditional, include
{id: jinja-loop-conditional}

```
.
├── app.py
└── templates
    ├── incl
    │   ├── footer.html
    │   └── header.html
    └── main.html
```

![](examples/flask/jinja/app.py)
![](examples/flask/jinja/templates/main.html)
![](examples/flask/jinja/templates/incl/header.html)
![](examples/flask/jinja/templates/incl/footer.html)


## Exercise: Flask persistent
{id: exercise-flask-persistent-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing.


## Exercise: Flask persistent
{id: exercise-flask-persistent-multi-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing. For each user have its own counter as identified by the username they type in.

## Flask Exercises
{id: flask-exercises}

* [Shopping list](https://code-maven.com/shopping-list)
* [TODO](https://code-maven.com/todo)


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

