# Flask route parameters - separate route to root page


One way to overcome the starnge situation that /user/Foo works but /user/ gives a 404 Not Found error is to add an extra route that
will specifically handle that case.

{% embed include file="src/examples/flask/path-separate/app.py" %}

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```

With the tests we can see that now /user/ works and returns the value we expected. Howerver there is anothe special address and that is
the /user path, the one without the trailing slash. Flask will handle this too by automatiocally redirecting the browser to the /user/ page.

You can see uisng the test case that the /user path returns a '308 Permanent Redirect' error and sets the "Location" in the response header.
Regular browsers would automatically move to the /user/ page and show the response from there.

Flask will also send some HTML content explaining the situation. This is only relevant for browsers, or other HTTP clients that don't automatically
follow the redirection.

For example curl will not automaticall follow this redirection. However if you supply the -L flag then it will.

curl -L http://127.0.0.1:5000/user

{% embed include file="src/examples/flask/path-separate/test_app.py" %}

