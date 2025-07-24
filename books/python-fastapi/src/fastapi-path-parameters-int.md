# FastAPI - Path Parameters - int



{% embed include file="src/examples/fastapi/userid-path/main.py" %}

```
http://localhost:8000/user/23      works
http://localhost:8000/user/foo     422 error
http://localhost:8000/user/2.3     422 error
```


