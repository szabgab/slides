# Docker: Perl Hello World


{% embed include file="src/examples/hello-world-perl/Dockerfile" %}

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello from Perl
```


