# Perl with Docker
{id: perl}

## Docker: Perl Hello World
{id: docker-perl-hello-world}

![](examples/hello-world-perl/Dockerfile)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello from Perl
```

## Docker: Perl Hello World in script
{id: docker-perl-script-hello-world}

![](examples/hello-world-perl-script/Dockerfile)

![](examples/hello-world-perl-script/hello_world.pl)

```
$ docker build -t mydocker .
$ docker run -it --rm mydocker
Hello World from Perl script
```

## Docker: Perl with I/O
{id: docker-perl-with-io}

![](examples/perl-io/Dockerfile)

![](examples/perl-io/greetings.pl)

```
$ docker build -t mydocker .
```

We need to tell Docker that this is an interactive process

```
docker run -it --rm mydocker

What is your name? Foo
Hello Foo, how are you today?
```


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


