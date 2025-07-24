# docker compose - keep running two ways


{% embed include file="src/examples/compose2/docker-compose.yml" %}
{% embed include file="src/examples/compose2/Dockerfile1" %}
{% embed include file="src/examples/compose2/Dockerfile2" %}

attach to either one of them:

```
docker-compose exec one sh
ping compose1_one_1
```


