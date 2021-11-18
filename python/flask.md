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

{aside}
There is nothing special. You install flask as you'd install any other Python package. Using some kind of virtual envrionment is recommended here too.
{/aside}

```
virtualenv venv -p python3
source venv/bin/activate

pip install flask
```

## Flask: Hello World
{id: flask-hello-world}
{i: Flask}
{i: route}
{i: app}

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
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ flask run
```

or

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

Other parameters

```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run --port 8080 --host 0.0.0.0
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
Showing a static text in the previous example was already a success, but we would like to be able to have a more dynamic web site.
In this example we'll see how to display the current time.

We have the same skeleton as in the previous example, but this time the `main` function serving the root path returns some HTML
that will be displayed as a link to the `/time` path.

We also have a second route mapping the `/time` path to the `show_time` function.

We run the application the same way as before on the command line.

Now if we access the `http://127.0.0.1:5000/` URL we'll see the text `time` that we can click on. When we click on it we arrive at the
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

{aside}
How can we test the version of our application that also has a generated page? We need to test two pages.

There are many ways to divide our tests.
* We could put all the tests in a single test-function.
* We could have two test-functions in the same test-file.
* We could have two test-functions in two separate test-files.

Putting them in separate functions allows us to run them separately. It also means that if one fails the other might still pass.
Usually we put independent test-cases in separate functions. Because it is still so small, putting them in two separate files seems to be an overkill.

The `test_home` function is relatively straight forward. We get the main page and then we check the status-code and the exact match for the content.

The `test_time` function is trickier. We can't check an exact match as the timestamp will be different every time we run the code. We could **mock**
the time, but we are looking for a simpler solution. So instead of an exact match we use a regexp to check if the result looks like a number we would
expect.

You can run the tests by running `pytest`.
{/aside}

![](examples/flask/time/test_app.py)

```
pytest
```

## Flask: Echo GET
{id: flask-echo-get}
{i: request}
{i: request.args}

{aside}
request.args is a dictionary. We could write request.args['name'] but then it would raise and excpetion and the whole application would crash
if the user did not send in a value for the "name" field. We could check if the key exists before trying to access the value using the "in" operator,
but that seems like a bit of a waste of work here. Instead we call the "get" method that every dictionary in Python has. It will return None, if the key "name"
did not exists. We could even provide a default value to the "get" method".
{/aside}


![](examples/flask/echo_get/app.py)

## Flask: Echo GET - testing
{id: flask-echo-get-testing}

![](examples/flask/echo_get/test_app.py)

## Flask: Echo GET - client
{id: flask-echo-get-client}
{i: requests}
{i: curl}

```
curl http://localhost:5000/
curl http://localhost:5000/echo?text=Sanch+Panza
```

![](examples/flask/echo_get/client.py)

## Flask: Echo POST
{id: flask-echo-post}
{i: request}
{i: request.form}

{aside}
There is also a dictionary called "request.form" that is get filled by data submitted using a POST request. This too is a plain Python dictionary.
In this case too we could use the "request.form.get('field', '')" call but instead of that we used the "in" operator and then the regular dicstionary look-up.
{/aside}

![](examples/flask/echo_post/app.py)

## Flask: Echo POST - testing
{id: flask-echo-post-testing}

![](examples/flask/echo_post/test_app.py)

## Flask: Echo POST - client
{id: flask-echo-post-client}
{i: request}
{i: request.form}
{i: curl}

```
curl --data "text=Sancho Panza" http://localhost:5000/echo
```

![](examples/flask/echo_post/client.py)

## Exercise: Flask calculator
{id: exercise-flask-calculator}

Write a web application that has two entry boxes and a button and
that will add the two numbers inserted into the entry boxes. Write two solutions.
In one of them the form will be submitted using GET in the other one it will be submitted using POST.

## Solution: Flask calculator
{id: solution-flask-calculator}

* See in the next few slides


## Flask GET and POST in two functions
{id: flask-get-and-post-in-two-functions}
{i: request}

![](examples/flask/separated-get-post/app.py)

## Flask GET and POST in two functions - testing
{id: flask-get-and-post-in-two-functions-testing}

![](examples/flask/separated-get-post/test_app.py)


## Flask GET and POST in one function
{id: flask-get-and-post-in-one-function}
{i: request.method}
{i: methods}

![](examples/flask/merged-get-post/app.py)


## Flask GET and POST in one function - testing
{id: flask-get-and-post-in-one-function-testing}

![](examples/flask/merged-get-post/test_app.py)

## Flask Logging
{id: flask-logging}

![](examples/flask/log/app.py)

## Flask URL routing
{id: flask-url-routing}

{aside}
The mapping of the path part of a URL, so the one that comes after the domain name and
after the port number (if it is included) is the path. Mapping that to a function call
is called routing.

In the following pages we are going to see several examples on how to map routes to functions.

It is also called "url route registration".
{/aside}

## Flask Path or route parameters
{id: flask-path-params}

{aside}
In addition to having routes for fixed pathes, Flask can also handle routes where one or more parts of the path can have any value.

It can be especially useful if the response is then looked up in some sort of a database.
{/aside}

![](examples/flask/path/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

## Flask Path or route parameters - testing
{id: flask-path-params-testing}

![](examples/flask/path/test_app.py)

* The route /user/ returns 404 not found

{aside}
The test here get a bit complex. We have 3 different tests function. Each one needs the variable returned by the `test_client` function.


While the route with the parameter can handle any value, there is one route that it does not handle. If the visitor reached the page /user/ page
either by mistake or by removing the parameter in the URL, then we'll see a "404 Not Found" page.
{/aside}


## Flask route parameters - separate route to root page
{id: flask-path-params-separate-route}

{aside}
One way to overcome the starnge situation that /user/Foo works but /user/ gives a 404 Not Found error is to add an extra route that
will specifically handle that case.
{/aside}

![](examples/flask/path-separate/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

{aside}
With the tests we can see that now /user/ works and returns the value we expected. Howerver there is anothe special address and that is
the /user path, the one without the trailing slash. Flask will handle this too by automatiocally redirecting the browser to the /user/ page.

You can see uisng the test case that the /user path returns a '308 Permanent Redirect' error and sets the "Location" in the response header.
Regular browsers would automatically move to the /user/ page and show the response from there.

Flask will also send some HTML content explaining the situation. This is only relevant for browsers, or other HTTP clients that don't automatically
follow the redirection.

For example curl will not automaticall follow this redirection. However if you supply the -L flag then it will.

curl -L http://127.0.0.1:5000/user
{/aside}

![](examples/flask/path-separate/test_app.py)

## Flask route parameters - default values
{id: flask-path-params-default-values}

![](examples/flask/path-default/app.py)
![](examples/flask/path-default/test_app.py)

## Flask Path or route parameters (int)
{id: flask-path-params-int}
{i: int}

![](examples/flask/path-int/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```


## Flask Path or route parameters add (int)
{id: flask-path-params-add-int}

![](examples/flask/path-int-add/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

## Flask Path or route parameters add (path)
{id: flask-path-params-any-path}
{i: path}

* Accept any path, including slashes:

![](examples/flask/path-any/app.py)

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

## Exercise: Calculator with path
{id: exercise-calculator-with-path}

* Write an application that works like a calculator based on the path:

```
/add/2/3    displays 2+3=5
/mul/3/4    displays 3*4=12
```

Then also add the following:

```
/sum/2/1.4/-78
```

* Write tests for each case

## Solution: Calculator with path
{id: solution-calculator-with-path}

![](examples/flask/path-int-add/app.py)
![](examples/flask/path-int-add/test_app.py)

## Flask Redirect
{id: flask-redirect}
{i: redirect}

* redirect(external url)

![](examples/flask/redirect/app.py)
![](examples/flask/redirect/test_app.py)

## Flask Internal Redirect with url_for
{id: flask-internal-redirect}
{i: redirect}
{i: url_for}

* url_for('login')  Returns the url based on the functions name

![](examples/flask/internal-redirect/app.py)
![](examples/flask/internal-redirect/test_app.py)

## Flask Internal Redirect with parameters
{id: flask-internal-redirect-parameters}

* url_for('login', key=value) Pass parameters to the URL path  keys that are not part of the route definitions will be converted to query string values

![](examples/flask/redirect-with-parameters/app.py)
![](examples/flask/redirect-with-parameters/test_app.py)


## Exercise: Random redirect
{id: exercise-random-redirect}

* Create an application that has a route called /random that will randomly redirect the visitor to on of several pre-defined URLs.
* Create your own list of pre-defined URLs.

## Solution: Random redirect
{id: solution-random-redirect}

* [random.choice](https://docs.python.org/3/library/random.html#random.choice)

![](examples/flask/random-redirect/app.py)
![](examples/flask/random-redirect/test_app.py)


## Flask Jinja template
{id: flask-templates}
{i: jinja}
{i: render_template}

* [Jinja](https://jinja.palletsprojects.com/)

![](examples/flask/jinja-plain/app.py)
![](examples/flask/jinja-plain/templates/index.html)

## Flask Jinja template - testing
{id: flask-templates-testing}

![](examples/flask/jinja-plain/test_app.py)

## Flask Jinja template with parameters
{id: flask-templates-parameters}

![](examples/flask/jinja-parameters/app.py)
![](examples/flask/jinja-parameters/templates/echo.html)
![](examples/flask/jinja-parameters/test_app.py)


## Flask Jinja template with conditional
{id: flask-templates-conditional}
{i: if}
{i: endif}

![](examples/flask/jinja-conditional/app.py)
![](examples/flask/jinja-conditional/templates/echo.html)
![](examples/flask/jinja-conditional/test_app.py)

## Flask Jinja template with loop
{id: flask-jinja-loop}
{i: for}
{i: in}
{i: endfo}

![](examples/flask/jinja-loop/app.py)
![](examples/flask/jinja-loop/templates/main.html)
![](examples/flask/jinja-loop/test_app.py)

## Flask Jinja template dictionary
{id: flask-jinja-dictionary}

![](examples/flask/jinja-dictionary/app.py)
![](examples/flask/jinja-dictionary/templates/main.html)
![](examples/flask/jinja-dictionary/test_app.py)


## Flask Jinja template list of dictionaries
{id: flask-jinja-list-of-dictionaries}

![](examples/flask/jinja-list-of-dictionaries/app.py)
![](examples/flask/jinja-list-of-dictionaries/templates/main.html)
![](examples/flask/jinja-list-of-dictionaries/test_app.py)


## Flask Jinja include
{id: flask-jinja-include}

```
.
├── app.py
├── test_app.py
└── templates
    ├── incl
    │   ├── footer.html
    │   └── header.html
    └── main.html
```

![](examples/flask/jinja-include/app.py)
![](examples/flask/jinja-include/templates/main.html)
![](examples/flask/jinja-include/templates/incl/header.html)
![](examples/flask/jinja-include/templates/incl/footer.html)

![](examples/flask/jinja-include/test_app.py)

## Jinja extend template layout block
{id: jinja-extend-template-layout}
{i: layout}
{i: extends}
{i: block}

{aside}
We use **extend** to connect between templates.
We use **block** both to mark the area that will be replaced and the content that will replace it.
{/aside}

![](examples/flask/template-extends/app.py)
![](examples/flask/template-extends/test_app.py)
![](examples/flask/template-extends/templates/index.html)
![](examples/flask/template-extends/templates/layouts/base.html)

## Jinja template inheritance - super
{id: jinja-template-inheritance}
{i: super}

* Using the **super()** call we can inherit the content of the block

![](examples/flask/template-inheritance/app.py)
![](examples/flask/template-inheritance/test_app.py)
![](examples/flask/template-inheritance/templates/index.html)
![](examples/flask/template-inheritance/templates/page.html)
![](examples/flask/template-inheritance/templates/layouts/base.html)

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


## Exercise: Flask persistent counter
{id: exercise-flask-persistent-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing.


## Exercise: Flask persistent multi-counter
{id: exercise-flask-persistent-multi-counter}


Create a Flask-based application with a persistent counter that even after restarting the application
the counter will keep increasing. For each user have its own counter as identified by the username they type in.

## Solution: Flask persistent counter
{id: solution-flask-persistent-counter}

![](examples/flask/persistent-counter/app.py)
![](examples/flask/persistent-counter/test_app.py)

## Solution: Flask persistent multi-counter
{id: solution-flask-persistent-multi-counter}

![](examples/flask/persistent-multi-counter/app.py)
![](examples/flask/persistent-multi-counter/test_app.py)



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
{i: jsonify}

![](examples/flask/20/app.py)

```
$ curl -I http://localhost:5000/api/info
HTTP/1.0 200 OK
Content-Type: application/json
```
![](examples/flask/20/test_app.py)

## Flask and AJAX with Vanila JavaScript
{id: flask-and-ajax-plain-javascript}
{i: jsonify}

![](examples/flask/21/app.py)
![](examples/flask/21/test_app.py)

![](examples/flask/21/static/math.js)
![](examples/flask/21/templates/main.html)


## Flask and AJAX with JQuery
{id: flask-and-ajax-jquery}
{i: jsonify}

![](examples/flask/22/app.py)
![](examples/flask/22/static/math.js)
![](examples/flask/22/templates/main.html)

## Flask POST JSON data to web application
{id: flask-post-json-data}

![](examples/flask/post-json/app.py)
![](examples/flask/post-json/test_app.py)


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


## Login
{id: login}

![](examples/flask/login/app.py)


## Configuratio
{id: flask-configuration}

* [Configuration](https://flask.palletsprojects.com/config)

* You can access and change it via the `app.config` dictionary in the applications code


