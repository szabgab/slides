# Flask custom 404 page

{% embed include file="src/examples/flask/404/app.py" %}
{% embed include file="src/examples/flask/404/app404.py" %}

```
curl -I http://localhost:5000/not

HTTP/1.0 404 NOT FOUND
```


