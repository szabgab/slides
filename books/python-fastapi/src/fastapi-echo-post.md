# FastAPI - Echo POST - request body

{% embed include file="src/examples/fastapi/echo-post/main.py" %}

```
http://localhost:8000/?text=Foo%20Bar
```

```
curl -d '{"text":"Foo Bar"}' -H "Content-Type: application/json" -X POST http://localhost:8000/
```

{% embed include file="src/examples/fastapi/echo-post/client.py" %}



