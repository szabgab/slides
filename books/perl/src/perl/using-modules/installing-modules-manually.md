# Installing modules manually

```
Download the tar.gz file from metacpan.org:

$ wget URL
$ tar xzf distribution.tar.gz
$ cd distribution
$ perl Makefile.PL
$ make
$ make test
$ make install  (as root or with sudo)
```

Without root rights


```
perl Makefile.PL PREFIX=/home/foobar/perlib LIB=/home/foobar/perlib/lib
```



