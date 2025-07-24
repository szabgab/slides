# FastAPI with Docker compose

{% embed include file="src/examples/fastapi/Dockerfile)

{% embed include file="src/examples/fastapi/docker-compose.yml)

{% embed include file="src/examples/fastapi/requirements.txt" %}

```
docker compose up
```

```
docker exec -it fastapi_app_1 bash
```

```
uvicorn main:app --reload --host=0.0.0.0
```


