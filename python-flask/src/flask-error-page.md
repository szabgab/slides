# Flask Error page


{% embed include file="src/examples/flask/500/app.py" %}

Will not trigger in debug mode!

```
$ FLASK_APP=echo.py FLASK_DEBUG=0  flask run
```

```
curl -I http://localhost:5000/not

HTTP/1.0 500 INTERNAL SERVER ERROR
```

{% embed include file="src/examples/flask/500/app500.py" %}



