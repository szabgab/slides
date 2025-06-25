# Flask generated page - time

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

{% embed include file="src/examples/flask/time/app.py" %}

```
FLASK_APP=app FLASK_DEBUG=1 flask run
```


