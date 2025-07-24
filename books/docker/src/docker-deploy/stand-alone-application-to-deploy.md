# Stand-alone Application to deploy


* A stand-alone Docker image that exposes a single port

{% embed include file="src/examples/deploy-stand-alone-python/app.py" %}
{% embed include file="src/examples/deploy-stand-alone-python/test_app.py" %}
{% embed include file="src/examples/deploy-stand-alone-python/requirements.txt" %}
{% embed include file="src/examples/deploy-stand-alone-python/Dockerfile" %}
{% embed include file="src/examples/deploy-stand-alone-python/.dockerignore" %}

Locally

```
docker build -t flasker .
docker run --rm  -p5000:5000 flasker
http://localhost:5000/
```


