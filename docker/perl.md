# Perl with Docker
{id: perl}

## Docker Perl Dancer hello world app
{id: docker-perl-dancer-hello-world-app}

## Developing Perl code in Docker
{id: developing-perl-code-in-docker}

```
$ docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/hw.pl
```

* Mount a directory of the host OS to a directory in the Docker image.
* Run the code

## Install Perl Modules
{id: install-perl-modules}

Install a perl module using *apt-get*

![](examples/perl-mechanize/Dockerfile)

![](examples/perl-mechanize/get.pl)

```
$ docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl
Usage: /opt/get.pl URL
```

```
docker run -v /Users/gabor/work/mydocker:/opt/  mydocker perl /opt/get.pl http://perlmaven.com/
```


