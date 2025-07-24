# Docker: Perl with I/O


{% embed include file="src/examples/perl-io/Dockerfile" %}

{% embed include file="src/examples/perl-io/greetings.pl" %}

```
$ docker build -t mydocker .
```

We need to tell Docker that this is an interactive process

```
docker run -it --rm mydocker

What is your name? Foo
Hello Foo, how are you today?
```


