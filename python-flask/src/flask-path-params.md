# Flask Path or route parameters

In addition to having routes for fixed pathes, Flask can also handle routes where one or more parts of the path can have any value.

It can be especially useful if the response is then looked up in some sort of a database.

{% embed include file="src/examples/flask/path/app.py" %}

```
FLASK_APP=app.py FLASK_DEBUG=0  flask run
```


