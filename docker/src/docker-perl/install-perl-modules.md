# Install Perl Modules

Install a perl module using *apt-get*

{% embed include file="src/examples/perl-mechanize/Dockerfile" %}

{% embed include file="src/examples/perl-mechanize/get.pl" %}

```
$ docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl
Usage: /opt/get.pl URL
```

```
docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl http://perlmaven.com/
```


