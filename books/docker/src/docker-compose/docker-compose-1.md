# Docker compose 1st example


provide command line override for CMD/ENTRYPOINT in the compose yaml file

{% embed include file="src/examples/compose1/docker-compose.yml" %}
{% embed include file="src/examples/compose1/Dockerfile" %}

```
cd examples/compose1
docker-compose up
```

* This builds the image based on the Dockerfile and then launches two containers


