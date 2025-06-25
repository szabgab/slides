# FastAPI mounted sub-applications


{% embed include file="src/examples/fastapi/mounted-applications/main.py" %}

{% embed include file="src/examples/fastapi/mounted-applications/api_v1.py" %}

```
uvicorn main:api_v1 --reload --host=0.0.0.0
uvicorn main:main --reload --host=0.0.0.0
```


