# Docker: Perl Hello World in script


{% embed include file="src/examples/hello-world-perl-script/Dockerfile" %}

{% embed include file="src/examples/hello-world-perl-script/hello_world.pl" %}

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello World from Perl script
```


