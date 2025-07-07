# Python, Flask and Pulsar

```
docker run -it -p 6650:6650 -p 8080:8080  apachepulsar/pulsar:2.4.1 bin/pulsar standalone
docker build -t mydocker .
docker run --rm -it mydocker bash
```

{% embed include file="src/examples/python-pulsar/docker-compose.yml" %}

{% embed include file="src/examples/python-pulsar/Dockerfile" %}

{% embed include file="src/examples/python-pulsar/pulsar_demo.py" %}


