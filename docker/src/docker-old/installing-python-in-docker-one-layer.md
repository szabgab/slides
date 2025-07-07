# Installing Python in Docker - one layer


The same as earlier, but now we merged the 3 RUN commands into one, so we have less levels in the history.


{% embed include file="src/examples/old-python-2/Dockerfile" %}

```
$ docker build -t mydocker2 .
```


